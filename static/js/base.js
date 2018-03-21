// 变量集合

function datatableInit(e, Source, Columns) {
    var data = arguments[3] ? arguments[3] : {};
    e.DataTable({
        // 默认基础选项
        // 控件的位置
        dom: '<"top"fl<"clear">>rt<"bottom"lip<"clear">>',

        // 是否延迟渲染
        bDeferRender: true,

        // 接口地址，如果没有fnServerData，则是get
        sAjaxSource: Source,
        // 有fnServerData，则是post，aoDate是所有相关数据
        fnServerData: function (sSource, aoData, fnCallback) {
            $.ajax({
                "dataType": 'json',
                "type": "POST",
                "url": sSource,
                "data": data,
                "success": fnCallback
            });
        },

        // 列的相关顺序，样式等等选择定义
        aoColumns: Columns,

        // 汉语化
        oLanguage:
            { //国际化配置
                "sProcessing": "正在处理中，请稍后...",
                "sLoadingRecords": "正在获取数据，请稍后...",
                "sLengthMenu": "显示 _MENU_ 条",
                "sZeroRecords": "没有您要搜索的内容",
                "sEmptyTable": "目前没有数据",
                "sInfo": "从第 _START_ 条记录到第  _END_ 条记录，总记录数为 _TOTAL_ 条",
                "sInfoEmpty": "记录数为0",
                "sInfoFiltered": "(全部记录数 _MAX_ 条)",
                "sInfoPostFix": "",
                "sSearch": "搜索",
                "sUrl": "",
                "oPaginate":
                    {
                        "sFirst": "首页",
                        "sPrevious": "上一页",
                        "sNext": "下一页",
                        "sLast": "末页"
                    },
                "oAria": {
                    "sSortAscending": "点击/返回升序排序",
                    "sSortDescending": "点击/返回降序排序"
                }
            },
        // 是否显示 处理中。。。
        bPagingage: true,

        // 是否保存状态信息到cookies
        bStateSave: true,

        // 分页样式
        sPaginationType: "full_numbers"

    });
}

// 更新按钮样式
function updateSwitch(e) {
    if (e === 'all') {
        $('.toggle-checkbox').bootstrapSwitch({
            size: "small"
        });
    }
    else {
        e.bootstrapSwitch({
            size: "small"
        })
    }
}

// 更新下拉框样式
function updateSelect(e) {
    if (e === 'all') {
        $('.select').select2({
            width: "200px",
            allowClear: true,
            placeholder: "请选择一个选项"
        })
    }
    else {
        e.select2({
            width: "200px",
            allowClear: true,
            placeholder: "请选择一个选项"
        })
    }
}

// 显示弹窗
function showToast(text) {
    $('#toast div.media-body').text(text);
    $('#toast').modal()
}

// 提示
$(function () {
    // $("[data-toggle='popover']").popover();

    // 下拉列表框的样式设置
    updateSelect('all');
});

