-- Find attrition rate by department
SELECT Department, 
       SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*) AS AttritionRate
FROM HR_Employee_Attrition
GROUP BY Department;

-- Average tenure of employees who left vs stayed
SELECT Attrition, AVG(YearsAtCompany) AS AvgTenure
FROM HR_Employee_Attrition
GROUP BY Attrition;
