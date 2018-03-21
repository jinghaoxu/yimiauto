select = """
SELECT
  suiteId,
  suiteName,
  modularName,
  createName,
  createTime,
  lastUpDate
FROM user_case_suite_data
  JOIN modular_config ON modularId = modularFId
  WHERE status = 1
  AND suiteName LIKE ? 
  AND modularName LIKE ?;
"""

suite_details = """
SELECT
  orders,
  caseName,
  caseSheet,
  suite_case_rel.status status,
  Remarks
FROM suite_case_rel
  JOIN user_case_data ON caseId = caseFid
WHERE suiteFid = ?;
"""
