select timestampdiff(hour, `employee_details`.`punch_out`, `employee_details`.`punch_in`);
select empid, timestampdiff(MINUTE,punch_in, punch_out) from employee_details group by empid;
select empid, sum(timestampdiff(MINUTE,punch_in, punch_out)) from employee_details group by empid;

select empid, timestampdiff(MINUTE, pi.punch_in, po.punch_out)/60 as  from employee e inner join punchin pi on e.empid = pi.empid
inner join punchout po on e.empid = po.empid group by e.empid having e.empid = 10;


select e.name, e.emp_id, SEC_TO_TIME(sum(timestampdiff(second, ed.punch_in, ed.punch_out))) from api_employeeloginmodel ed inner join  api_employeemodel e on ed.emp_id_id = e.emp_id group by ed.emp_id_id, e.name;

 select e.name, e.emp_id, SEC_TO_TIME(sum(timestampdiff(second, ed.punch_in, ed.punch_out))) 
 as 'Total Working Hours' from api_employeeloginmodel ed inner join  
 api_employeemodel e on ed.emp_id_id = e.emp_id group by ed.emp_id_id, e.name having e.emp_id = 10;