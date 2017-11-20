from dateutil.relativedelta import relativedelta
from edc_visit_schedule.schedule import Schedule


crfs = ()

requisitions = ()

schedule1 = Schedule(
    name='schedule1',
    app_label='amp',
    enrollment_model='amp.enrollment',
    disenrollment_model='amp.disenrollment',
    visit_model='amp.subjectvisit',
    offstudy_model='amp.subjectoffstudy',
    verbose_name='Amp Visit Schedule',
)


visit_codes = [
    '1', '2', '3', '4', '5', '6', '7', '8',
    '9', '10', '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20', '21', '22', '23',
    '24', '25', '26', '31', '32', '33', '34',
    '35', '47', '48', '71', '72', '73', '74',
    '75', '76', '77', '78']

for code in visit_codes:
    # add visits to this schedule
    schedule1.add_visit(
        code=code,
        title='Visit' + code,
        timepoint=code,
        rbase=relativedelta(months=int(code)),  # TO DO confirm
        rlower=relativedelta(months=0),
        rupper=relativedelta(months=0),
        requisitions=requisitions,
        crfs=crfs)
