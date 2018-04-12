/**
 * Created by xdao07 on 2018/3/27.
 */

//KindEditor.ready(function(K) {
//    K.create('#id_content', {
//        //个性化定制内容，更多内容参数官方文档
//        width: 800,
//        height: 600,
//    });
//});

KindEditor.ready(function(K) {
    K.create('textarea[name="content"]', {
        //个性化定制内容，更多内容参数官方文档
        width: 800,
        height: 600,
        uploadJson: '/admin/upload/kindeditor',  //指定上传文件的服务器端程序,(默认值: basePath + ‘php/upload_json.php’)，此处通过urls.py映射到指定程序
    });
});
