set lines 300 pages 4000 head off feed off colsep ',' und off
set trimspool on

spool rman.csv

--select 'TYPE,STATUS,START,END' from dual
--union all
--SELECT 
--    input_type ||','||
--    decode(status,'COMPLETED','OK','COMPLETED WITH WARNINGS','OK','FAILED','NOK','RUNNING','RUN','UNK') ||','||
--    start_time ||','||
--    end_time   
--FROM  STATS_RMAN
--WHERE to_date(start_time,'YYYY-MM-DD HH24:MI:SS') > trunc(sysdate, 'mm');


select 'TYPE,STATUS,START,END' from dual
union all
SELECT 
    input_type ||','||
    decode(status,'COMPLETED','OK','COMPLETED WITH WARNINGS','OK','FAILED','NOK','RUNNING','RUN','UNK') ||','||
    TO_CHAR(start_time,'YYYY-MM-DD HH24:MI:SS') ||','||
    TO_CHAR(end_time,'YYYY-MM-DD HH24:MI:SS')   
FROM  V$RMAN_BACKUP_JOB_DETAILS
WHERE start_time > trunc(sysdate, 'mm');

exit;