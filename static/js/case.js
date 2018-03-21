$(function () {
    // datatable数据加载
    var caseTable = datatableInit(
        $("#case_table"),
        '../casedata',
        [
            {"mData": "caseId"},
            {"mData": "caseName"},
            {"mData": "modularName"},
            {"mData": "caseSheet"},
            {"mData": "Remarks"},
            {"mData": "createName"},
            {"mData": "createTime"},
            {"mData": "lastUpDate"}
        ],
        {
            'suiteid': suiteid,
            'modularid': modularid
        });

    // 恢复默认 按钮事件
    $('#default').click(function () {
        // 清除指定缓存
        localStorage.removeItem('DataTables_case_table_/case.html/');

        // 页面刷新 F5
        window.location.reload();
    });

    // 相关用例 按钮事件
    $('#related_cases').click(function () {
        console.log(2)
    });

    // 详情 按钮事件
    $('#details').click(function () {
        console.log(3)
    });

    // 相关报告 按钮事件
    $('#related_reports').click(function () {
        console.log(4)
    });

    // 列表数据选择事件
    $(function () {
        $('table tbody').on('click', 'tr', function () {
            $('.selected').removeClass('selected');
            $(this).toggleClass('selected');
        });
    });
});
