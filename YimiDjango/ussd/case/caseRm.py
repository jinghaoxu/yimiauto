"""
用例页面读取数据库操作
"""

select = {
    'base1': """
            SELECT
              caseId,
              caseName,
              ucd.createName,
              ucd.createTime,
              ucd.lastUpDate,
              modularName,
              ucd.Remarks,
              caseSheet
            FROM user_case_data ucd
              JOIN modular_config ON modularId = modularFid """,
    'suite1': 'LEFT JOIN suite_case_rel ON caseId = caseFid ',
    'base2': 'WHERE ucd.status = 1 ',
    'casename1': 'AND ucd.caseName LIKE ?',
    'suite2': ' AND suiteFid LIKE ? ',
    'modularid1': 'AND modularid LIKE ? ',
    'end': ';'
}
