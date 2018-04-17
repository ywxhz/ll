/**
 * Created by langusui on 2018/4/13.
 */

var idindex=11000;
var allPages=0;
var currentPage=1;
var tallNum=0;
var maxResult=0;
function formatterDateTime() {
  var date=new Date();
  var month=date.getMonth() + 1;
        var datetime = date.getFullYear()
                + ""// "年"
                + (month >= 10 ? month : "0"+ month)
                + ""// "月"
                + (date.getDate() < 10 ? "0" + date.getDate() : date
                        .getDate())
                + ""
                + (date.getHours() < 10 ? "0" + date.getHours() : date
                        .getHours())
                + ""
                + (date.getMinutes() < 10 ? "0" + date.getMinutes() : date
                        .getMinutes())
                + ""
                + (date.getSeconds() < 10 ? "0" + date.getSeconds() : date
                        .getSeconds());
        return datetime;
}
function hotelclick() {
    var cityname='长沙';
    var hotalname= $("#apitxtin").val() ;
    gethotelapi(cityname,hotalname);
}
function pointclick() {
    var cityid='199';
    var pointname='';
    getpointapi(cityid,pointname);
}
function gethotelpic(hotalid) {
    var hotelpicurl;
    var xx=formatterDateTime();
    var strurl="https://route.showapi.com/1450-3?hotalId="+hotalid+"&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp="+formatterDateTime()+"&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c";
    $.ajaxSettings.async = false
    $.getJSON(strurl, function(data) {
        //alert("1 hotalid "+hotalid);
        var i=0;
        $.each(data, function(key, field){
            //alert("1_" + field.toString() + " " + key.toString()+" i"+i.toString());
            if(key.toString()=="showapi_res_body" ){
                $.each(field, function(key1, field1){
                    //alert("2_" + field1.toString() + " " + key1.toString());
                    if(key1.toString()=="imgList" ) {
                        $.each(field1, function (key2, field2) {
                            $.each(field2, function (key3, field3) {
                                //alert("2_" + field3.toString() + " " + field3.toString());
                                if(field3.toString() =="外观"){
                                    $.each(field2, function (key3, field3) {
                                          if(key3.toString() =="imgUrl"){
                                              hotelpicurl=field3.toString();
                                              return false;
                                          }
                                     });
                                }
                            });
                        });
                    }
                });
            }
        });
    })
    //alert("hotelpicurl "+hotelpicurl)
    return  hotelpicurl;
}

//通过城市名称查询酒店
function gethotelapi(cityname,hotalname) {
    // alert("1");
   // var cityname="长沙";
     $("#dipIn").empty();
    //hotalname="";
    var xx=formatterDateTime();
    var strurl="https://route.showapi.com/1450-1?cityName="+cityname+"&hotalId=&hotalName="+hotalname+"&page="+currentPage+"&proName=&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp="+formatterDateTime()+"&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c";
    var proName;
    var cityName;
    var hotalName;
    var hotalpic;
    var hotalId;
    $.getJSON(strurl, function(data) {
            //alert("1 "+data.toString());
            var i=0;
            $.each(data, function(key, field){
                //alert("2_" + field.toString() + " " + key.toString()+" i"+i.toString());
                if(i==2){
                    $.each(field, function(key1, field1) {
                        //alert("3_ " + field1.toString() + " " + key1.toString());
                        if(key1.toString()=="allPages"){
                            allPages=field1.toString() ;
                        }
                         if(key1.toString()=="currentPage"){
                            currentPage=field1.toString() ;
                        }
                        if(key1.toString()=="tallNum"){
                            tallNum=field1.toString() ;
                        }
                        if(key1.toString()=="maxResult"){
                            maxResult=field1.toString() ;
                        }
                        if(key1.toString()=="contentlist"){
                             $.each(field1, function(key2, field2) {
                                //输出每行
                                $.each(field2, function(key3, field3) {
                                    if(key3.toString()=="proName"){
                                        proName=field3.toString() ;
                                    }
                                    if(key3.toString()=="cityName"){
                                          cityName=field3.toString() ;
                                    }
                                    if(key3.toString()=="hotalName"){
                                          hotalName=field3.toString() ;
                                    }
                                    if(key3.toString()=="hotalId"){
                                        hotalId=field3.toString() ;
                                        hotalpic= gethotelpic(hotalId);
                                    }
                                 });
                                 $("#dipIn").append(gethotelrowhtml(proName,cityName,hotalName,hotalpic));
                             });
                        }
                    });
                }
                i++;
            });
             $("#dipIn").append(gethotelFYhtml(cityname,hotalname));
        })
}
function gethotelrowhtml(proName,cityName,hotalName,hotalpic) {

        var htmlstr1="";
        htmlstr1+="<a href=\"#\" id=\""+idindex.toString()+"\" class=\"list-group-item\" >";
        htmlstr1+="<div class=\"media\">";
        htmlstr1+="<div class=\"media-left\">";
        htmlstr1+="<img  src='"+hotalpic+"' style=\"height:85px;width:85px;\" />";
        htmlstr1+="</div>";
        htmlstr1+="<div class=\"media-body media-middle\">";
        htmlstr1+="<h4  class=\"list-group-item-heading\">"+hotalName+"</h4>";
        htmlstr1+="<p class=\"list-group-item-text\">省份:"+proName+"   城市:"+cityName+"</p>";
        htmlstr1+="</div>";
        htmlstr1+="<div class=\"media-right media-middle\">";
        htmlstr1+="<span class=\"badge\" onclick=\"do_addPoint('"+idindex.toString()+"')\"><h4>+</h4></span>";
        htmlstr1+="</div>";
        htmlstr1+="</div>";
        htmlstr1+="</a>";
        idindex++;
        return htmlstr1;
}
function gethotelFYhtml(cityname,hotalname) {
        var htmlstr1="";
        htmlstr1+="<div  style='text-align:right;' ><button onclick=\"do_FYHotelF('"+cityname+"','"+hotalname+"','B')\")>上一页</button><button onclick=\"do_FYHotelF('"+cityname+"','"+hotalname+"','F')\" >下一页</button> 当前第"+currentPage.toString()+"页，总共"+allPages.toString()+"页&nbsp&nbsp";
        htmlstr1+="</div>";
        return htmlstr1;
}
function  do_FYHotelF(cityname,hotalname,action) {
    if(action=="B"){
        if(parseInt(currentPage)!=1){
            currentPage--;
            gethotelapi(cityname,hotalname);
        }
    }
    if(action=="F"){
       if(parseInt(currentPage)<parseInt(allPages)){
            currentPage++;
           gethotelapi(cityname,hotalname);
       }

    }
}

//通过城市名称查询酒店
function getpointapi(cityid,pointname) {
    // alert("1");
   // var cityname="长沙";
     $("#dipIn").empty();
    //pointname="";
    var xx=formatterDateTime();
    var strurl="https://route.showapi.com/268-1?areaId=&cityId="+cityid+"&keyword="+pointname+"&page="+currentPage+"&proId=&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp="+formatterDateTime()+"&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c";
    var name;
    var areaName;
    var proName;
    var cityName;
    var address;
    var summary;
    var picUrlSmall;
    $.getJSON(strurl, function(data) {
            //alert("1 "+data.toString());
            var i=0;
            $.each(data, function(key, field){
                //alert("2_" + field.toString() + " " + key.toString()+" i"+i.toString());
                if( key.toString()=="showapi_res_body"){
                    $.each(field, function(key1, field1) {
                        //alert("3_ " + field1.toString() + " " + key1.toString());
                        if(key1.toString()=="pagebean"){
                              $.each(field1, function(key2, field2) {
                                   //alert("4_ " + field2.toString() + " " + key2.toString());
                                    if(key2.toString()=="contentlist"){
                                         $.each(field2, function(key3, field3) {
                                             //alert("5_ " + field3.toString() + " " + key3.toString());
                                             $.each(field3, function(key4, field4) {
                                                // alert("6_ " + field4.toString() + " " + key4.toString());
                                                 if(key4.toString()=="name"){
                                                     name=field4.toString() ;
                                                 }
                                                 if(key4.toString()=="areaName"){
                                                        areaName=field4.toString() ;
                                                 }
                                                 if(key4.toString()=="proName"){
                                                        proName=field4.toString() ;
                                                 }
                                                 if(key4.toString()=="address"){
                                                     address=field4.toString() ;
                                                 }
                                                 if(key4.toString()=="summary"){
                                                     summary=field4.toString() ;
                                                 }
                                                 if(key4.toString()=="cityName"){
                                                     cityName=field4.toString() ;
                                                 }
                                                 if(key4.toString()=="picList"){
                                                     $.each(field4, function(key5, field5) {
                                                             $.each(field5, function(key6, field6) {
                                                                 //alert("7_ " + field6.toString() + " " + key6.toString());
                                                                 if(key6.toString()=="picUrlSmall"){
                                                                        picUrlSmall=field6.toString()
                                                                        return false;
                                                                 }
                                                             });
                                                     });
                                                 }
                                             });
                                             //输出每行
                                               $("#dipIn").append(getpointrowhtml(name,areaName,proName,cityName,address,summary,picUrlSmall));
                                         });
                                    }
                                     if(key2.toString()=="allPages"){
                                        allPages=field2.toString() ;
                                     }
                                     if(key2.toString()=="currentPage"){
                                        currentPage=field2.toString() ;
                                    }
                                    if(key2.toString()=="allNum"){
                                        allNum=field2.toString() ;
                                    }
                                    if(key2.toString()=="maxResult"){
                                        maxResult=field2.toString() ;
                                    }
                                    // if(key1.toString()=="contentlist"){
                                    //      $.each(field1, function(key2, field2) {
                                    //          alert("4_ " + field2.toString() + " " + key2.toString());
                                    //         //输出每行
                                    //      });
                                    // }

                              });
                        }

                    });
                }
                i++;
            });
             $("#dipIn").append(getpointFYhtml(cityid,pointname));
        })
}
function getpointrowhtml(name,areaName,proName,cityName,address,summary,picUrlSmall) {
        var htmlstr1="";
        htmlstr1+="<a href=\"#\" id=\""+idindex.toString()+"\" class=\"list-group-item\" >";
        htmlstr1+="<div class=\"media\">";
        htmlstr1+="<div class=\"media-left\">";
        htmlstr1+="<img  src='"+picUrlSmall+"' style=\"height:85px;width:85px;\" />";
        htmlstr1+="</div>";
        htmlstr1+="<div class=\"media-body media-middle\">";
        htmlstr1+="<h4  class=\"list-group-item-heading\">"+name+"</h4>";
        htmlstr1+="<p class=\"list-group-item-text\">介绍:"+summary+"</p>";
        htmlstr1+="<p class=\"list-group-item-text\">省份:"+proName+"   城市:"+cityName+" 区域:"+areaName+" 地址:"+address+" </p>";
        htmlstr1+="</div>";
        htmlstr1+="<div class=\"media-right media-middle\">";
        htmlstr1+="<span class=\"badge\" onclick=\"do_addPoint('"+idindex.toString()+"')\"><h4>+</h4></span>";
        htmlstr1+="</div>";
        htmlstr1+="</div>";
        htmlstr1+="</a>";
        idindex++;
        return htmlstr1;
}
function getpointFYhtml(cityid,pointname) {
        var htmlstr1="";
        htmlstr1+="<div style='text-align:right;' ><button onclick=\"do_FYpointF('"+cityid+"','"+pointname+"','B')\")>上一页</button><button onclick=\"do_FYpointF('"+cityid+"','"+pointname+"','F')\" >下一页</button> 当前第"+currentPage.toString()+"页，总共"+allPages.toString()+"页&nbsp&nbsp";
        htmlstr1+="</div>";
        return htmlstr1;
}
function  do_FYpointF(cityid,pointname,action) {
    if(action=="B"){
        if(parseInt(currentPage)!=1){
            currentPage--;
            getpointapi(cityid,pointname);
        }
    }
    if(action=="F"){
       if(parseInt(currentPage)<parseInt(allPages)){
            currentPage++;
           getpointapi(cityid,pointname);
       }

    }
}


// //通过景点名称查询景点
// function getjdapi(jname) {
//     var xx=formatterDateTime();
//     alert(xx.toString());
//     var strurl="https://route.showapi.com/268-1?areaId=&cityId=&keyword="+jname+"&page=&proId=&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp="+formatterDateTime()+"&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c";
//     $.ajax({url:strurl,success:function(result){
//         alert(result.toString());
//     }});
// }


// //通过城市名称查询酒店
// function gethotelapi(cityname) {
//     // alert("1");
//    // var cityname="长沙";
//     var xx=formatterDateTime();
//     alert(xx.toString());
//     var strurl="https://route.showapi.com/1450-1?cityName="+cityname+"&hotalId=&hotalName=&page=&proName=&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp="+formatterDateTime()+"&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c";
//     $.ajax({url:strurl,success:function(result){
//         alert(result.toString());
//     }});
// }
// //通过景点名称查询景点
// function getjdapi(jname) {
//     var xx=formatterDateTime();
//     alert(xx.toString());
//     var strurl="https://route.showapi.com/268-1?areaId=&cityId=&keyword="+jname+"&page=&proId=&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp="+formatterDateTime()+"&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c";
//     $.ajax({url:strurl,success:function(result){
//         alert(result.toString());
//     }});
// }

