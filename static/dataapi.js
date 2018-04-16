/**
 * Created by langusui on 2018/4/13.
 */

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
//通过城市名称查询酒店
function gethotelapi(cityname) {
    // alert("1");
   // var cityname="长沙";
    var xx=formatterDateTime();
    alert(xx.toString());
    var strurl="https://route.showapi.com/1450-1?cityName="+cityname+"&hotalId=&hotalName=&page=&proName=&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp="+formatterDateTime()+"&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c";
    $.ajax({url:strurl,success:function(result){
        alert(result.toString());
    }});
}
//通过景点名称查询景点
function getjdapi(jname) {
    var xx=formatterDateTime();
    alert(xx.toString());
    var strurl="https://route.showapi.com/268-1?areaId=&cityId=&keyword="+jname+"&page=&proId=&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp="+formatterDateTime()+"&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c";
    $.ajax({url:strurl,success:function(result){
        alert(result.toString());
    }});
}
function getjdapix(){
    alert("xx");
    var strurl="https://route.showapi.com/1450-1?cityName=长沙&hotalId=&hotalName=&page=&proName=&showapi_appid=59865&showapi_test_draft=false&showapi_timestamp=20180413175356&showapi_sign=1c0eda05ab15436d8c6b5c9dbe1e023c";
    $.ajax({url:strurl,success:function(result){
          alert(result.toString());
    }});
}
// function getjdapi(cityname,page) {
//
// }
// function getjdapi(cityname,hotalname) {
//
// }