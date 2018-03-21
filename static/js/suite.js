$(function () {
/////////////////////////////////////////////
    // 变量集合
    // 新建、编辑 用例集用例列表数据的数量,一直累加，初始为0
    var newcasenum = 0;
    var editcasenum = 0;

    // 查询项的值
    var suitename = $('#suitename').val();
    var suitemodular = $('#suitemodular').val();
    // datatable数据加载
    var suiteTable = datatableInit(
        $("#suite_table"),
        '../suitedata',
        [
            {"mData": "suiteId"},
            {"mData": "suiteName"},
            {"mData": "modularName"},
            {"mData": "createName"},
            {"mData": "createTime"},
            {"mData": "lastUpDate"}
        ],
        {
            'suitename': suitename,
            'suitemodular': suitemodular
        }
    );
/////////////////////////////////////////////
    // 列表数据选择事件
    $(function () {
        $('#suite_table tbody').on('click', 'tr', function () {
            var flag = $(this).hasClass('selected');
            if (flag === true) {
                $('#suite_table .selected').removeClass('selected');
            }
            else {
                $('#suite_table .selected').removeClass('selected');
                $(this).toggleClass('selected');
            }
        });
        $('#newaddcasetable tbody').on('click', 'tr', function () {
            var flag = $(this).hasClass('success');
            if (flag === true) {
                $('#newaddcasetable .success').removeClass('success');
            }
            else {
                $('#newaddcasetable .success').removeClass('success');
                $(this).toggleClass('success');
            }
        });
        $('#editaddcasetable tbody').on('click', 'tr', function () {
            var flag = $(this).hasClass('success');
            if (flag === true) {
                $('#editaddcasetable .success').removeClass('success');
            }
            else {
                $('#editaddcasetable .success').removeClass('success');
                $(this).toggleClass('success');
            }
        });
    });

    // 恢复默认 按钮事件
    $('#default').click(function () {
        // 清除指定缓存
        localStorage.removeItem('DataTables_suite_table_/suite.html/');

        // 页面刷新 F5
        window.location.reload();
    });

    // 相关用例 按钮事件
    $('#related_cases').click(function () {
            var sele_num = $("#suite_table").find("tr.selected").length;
            if (sele_num === 1) {
                var suiteid = $("#suite_table").find("tr.selected td:first").text();
                $(this).attr('href', '../case.html/?suiteid=' + suiteid)
            }
            else {
                showToast('请选择一条数据！')
            }
        }
    );

    // 详情 按钮事件
    $('#details').click(function () {
        var sele_num = $("#suite_table").find("tr.selected").length;
        if (sele_num === 1) {
            // $(this).popover("hide");
            $("#suite_details_table").dataTable().fnDestroy();
            var nums = $("#suite_table").find("tr.selected td:first").text();
            var details = datatableInit(
                $("#suite_details_table"),
                '../get_suite_details',
                [
                    {"mData": "orders"},
                    {"mData": "caseName"},
                    {"mData": "caseSheet"},
                    {"mData": "status"},
                    {"mData": "Remarks"}
                ],
                {'nums': nums});
            $("#suitedetails").modal();
        }
        else {
            showToast('麻烦请选择一条数据！')
        }
    });

    // 相关报告 按钮事件
    $('#related_reports').click(function () {
    });

    // 查询按钮 事件
    $('#select').click(function () {
        get_select()
    });

    // 清空按钮 事件
    $('#clear').click(function () {
        $('#suitename').val("");
        $('#suitemodular').val("");
        get_select()
    });
/////////////////////////////////////////////
    /*监听输入框的回车操作*/
    $("#suitename,#suitemodular").keyup(function (e) {
        var eCode = e.keyCode ? e.keyCode : e.which ? e.which : e.charCode;
        if (eCode === 13) {
            get_select()
        }
    });

    // 查询方法
    function get_select() {
        var suitename = $('#suitename').val();
        var suitemodular = $('#suitemodular').val();
        $("#suite_table").dataTable().fnDestroy();
        var suiteTable = datatableInit(
            $("#suite_table"),
            '../suitedata',
            [
                {"mData": "suiteId"},
                {"mData": "suiteName"},
                {"mData": "modularName"},
                {"mData": "createName"},
                {"mData": "createTime"},
                {"mData": "lastUpDate"}
            ],
            {
                'suitename': suitename,
                'suitemodular': suitemodular
            }
        )
    }

/////////////////////////////////////////////
    // 新建按钮事件
    $('#new').click(function () {
        $('#suitenew').modal()
    });

    // 是否选择 按钮事件，更新下拉列表
    $('#newisselect').on('switchChange.bootstrapSwitch', function (e, s) {
        console.log(s);
    });

    // 返回添加的元素
    function getnewelement(num) {
        return "<tr>\n" +
            "                                        <th>\n" +
            "                                            <select title=\"选择用例\" id=\"newcaseselect" + num + "\" class=\"select\">\n" +
            "                                                <option value=\"flase\"> - 请选择 - </option>\n" +
            "                                            </select>\n" +
            "                                            <label for=\"newisrun" + num + "\" style=\"padding-left: 30px\">是否运行：</label>\n" +
            "                                            <input type=\"checkbox\" class=\"toggle-checkbox\" id=\"newisrun" + num + "\">\n" +
            "                                        </th>\n" +
            "                                    </tr>"
    }

    // 添加-前 按钮事件
    $('#newaddcaseafter').click(function () {
        var num = $('#newaddcasetable tr').length;
        if (num >= 4) {
            showToast('最多只能添加4条用例！')
        }
        else if ($('#newaddcasetable tr.success').length === 1) {
            newcasenum++;
            $('#newaddcasetable tr.success').after(getnewelement(newcasenum));
            updateSelect($('#newcaseselect' + newcasenum));
            updateSwitch($('#newisrun' + newcasenum));
        }
        else {
            newcasenum++;
            $('#newaddcasetable').append(getnewelement(newcasenum));
            updateSelect($('#newcaseselect' + newcasenum));
            updateSwitch($('#newisrun' + newcasenum));
        }
    });
    // 添加-后 按钮事件
    $('#newaddcasebefore').click(function () {
        var num = $('#newaddcasetable tr').length;
        if (num >= 4) {
            showToast('最多只能添加4条用例！')
        }
        else if ($('#newaddcasetable tr.success').length === 1) {
            newcasenum++;
            $('#newaddcasetable tr.success').before(getelement(newcasenum));
            updateSelect($('#newcaseselect' + newcasenum));
            updateSwitch($('#newisrun' + newcasenum));
        }
        else {
            newcasenum++;
            $('#newaddcasetable').append(getelement(newcasenum));
            updateSelect($('#newcaseselect' + newcasenum));
            updateSwitch($('#newisrun' + newcasenum));
        }
    })

    ;

    // 删除按钮事件
    $('#newdeletecase').click(function () {
        var flag = $('#newaddcasetable tr.success').length;
        if (flag === 1) {
            $('#newaddcasetable tr.success').remove();
        }
        else {
            showToast('麻烦选择一条数据！')
        }
    });

    // 提交按钮 事件
    $('#newsubmit').click(function () {
        showToast('提交')
    });

    // 关闭按钮 事件
    $('#newquit').click(function () {
        $('#newsuitename').val('');
        $('#newselectmodular').val('flase');
        $('#newisselect').bootstrapSwitch('state', false);
        $('#newaddcasetable tr').remove();
        $('#newaddcasetable').append(getelement(newcasenum));
        updateSelect($('#newcaseselect' + newcasenum));
        updateSwitch($('#newisrun' + newcasenum));
        updateSelect($('#newselectmodular'));
        $('#newmark').val('')
    });
/////////////////////////////////////////////

    // 编辑按钮事件
    $('#edit').click(function () {
        var sele_num = $("#suite_table").find("tr.selected").length;
        if (sele_num === 1) {
            var nums = $("#suite_table").find("tr.selected td:first").text();
            $('#suiteedit').modal()
        }
        else {
            showToast('请选择一条数据！')
        }
    });
    // 是否选择 按钮事件，更新下拉列表
    $('#editisselect').on('switchChange.bootstrapSwitch', function (e, s) {
        console.log(s);
    });

    // 返回添加的元素
    function geteditelement(num) {
        return "<tr>\n" +
            "                                        <th>\n" +
            "                                            <select title=\"选择用例\" id=\"editcaseselect" + num + "\" class=\"select\">\n" +
            "                                                <option value=\"flase\"> - 请选择 - </option>\n" +
            "                                            </select>\n" +
            "                                            <label for=\"editisrun" + num + "\" style=\"padding-left: 30px\">是否运行：</label>\n" +
            "                                            <input type=\"checkbox\" class=\"toggle-checkbox\" id=\"editisrun" + num + "\">\n" +
            "                                        </th>\n" +
            "                                    </tr>"
    }

    // 添加-前 按钮事件
    $('#editaddcaseafter').click(function () {
        var num = $('#editaddcasetable tr').length;
        if (num >= 4) {
            showToast('最多只能添加4条用例！')
        }
        else if ($('#editaddcasetable tr.success').length === 1) {
            editcasenum++;
            $('#editaddcasetable tr.success').after(geteditelement(editcasenum));
            updateSelect($('#editcaseselect' + editcasenum));
            updateSwitch($('#editisrun' + editcasenum));
        }
        else {
            editcasenum++;
            $('#editaddcasetable').append(geteditelement(editcasenum));
            updateSelect($('#editcaseselect' + editcasenum));
            updateSwitch($('#editisrun' + editcasenum));
        }
    });
    // 添加-后 按钮事件
    $('#editaddcasebefore').click(function () {
        var num = $('#editaddcasetable tr').length;
        if (num >= 4) {
            showToast('最多只能添加4条用例！')
        }
        else if ($('#editaddcasetable tr.success').length === 1) {
            editcasenum++;
            $('#editaddcasetable tr.success').before(geteditelement(editcasenum));
            updateSelect($('#editcaseselect' + editcasenum));
            updateSwitch($('#editisrun' + editcasenum));
        }
        else {
            editcasenum++;
            $('#editaddcasetable').append(geteditelement(editcasenum));
            updateSelect($('#editcaseselect' + editcasenum));
            updateSwitch($('#editisrun' + editcasenum));
        }
    })

    ;

    // 删除按钮事件
    $('#editdeletecase').click(function () {
        var flag = $('#editaddcasetable tr.success').length;
        if (flag === 1) {
            $('#editaddcasetable tr.success').remove();
        }
        else {
            showToast('麻烦选择一条数据！')
        }
    });

    // 提交按钮 事件
    $('#editsubmit').click(function () {
        showToast('提交')
    });

    // 关闭按钮 事件 无，点击编辑按钮时自动填充数据
    // $('#editquit').click(function () {
    //     $('#editsuitename').val('');
    //     $('#editselectmodular').val('flase');
    //     $('#editisselect').bootstrapSwitch('state', false);
    //     $('#editaddcasetable tr').remove();
    //     $('#editaddcasetable').append(getelement(editcasenum));
    //     updateSelect($('#editcaseselect' + editcasenum));
    //     updateSwitch($('#editisrun' + editcasenum));
    //     updateSelect($('#editselectmodular'));
    //     $('#editmark').val('')
    // });
/////////////////////////////////////////////

    // // 删除 按钮 事件
    // $('[name=delete]').click(function () {
    //     $(this).parent().parent().remove();
    // })
});
