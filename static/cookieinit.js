/**
 * Created by langusui on 2018/4/25.
 */
//判断cookie登录状态并执行相关方法
// $(document).ready(function () {
//     initcookie();
// })
window.onload = function () {
    initcookie();
}

function initcookie() {
    var psd = $.cookie('password');
    var url = "/checkin?psd=" + psd;
    //调取服务判断密码是否正确
    $.getJSON(url, function (data) {
        //调取服务判断密码是否正确
        if (data == '1') {
            $("#basepsddiv").hide();
        } else {
            $("#basepsddiv").show();
        }
    })
    // var strthml = "";
    // strthml += "<div id=\"basepsddiv\" style=\"position:absolute;width:100%;height:100%;z-index:99999999;background-color: #FFFFFF;opacity:0.7\">";
    // strthml += "<div style=\"position:absolute;left:45%;top:45%;opacity:1\">";
    // strthml += "输入密码:&nbsp<input id=\"cookiepsd\" type=\"password\" width=\"200px\" />";
    // strthml += "<button type=\"button\" onclick=\"setcookie()\" >确认</button></div>";
    // strthml += "</div>";
}
function setcookie(){
    //$(document.body).empty();
    var cval= $("#cookieinpsd").val()
    var url="/checkin?psd="+cval;
    $.getJSON(url, function(data) {
      //调取服务判断密码是否正确
        if(data == '1'){
            $.cookie('password',cval, { expires: 7 });
            $("#basepsddiv").hide();
        }else{
            alert("密码错误");
        }
    })
}
