from apscheduler.schedulers.background import BackgroundScheduler
from email_sender import send_custom_email

scheduler = BackgroundScheduler()

def schedule_email(email_data, send_time):
    job = scheduler.add_job(send_custom_email, 'date', run_date=send_time, args=[email_data])
    scheduler.start()
    return {"status": "Scheduled", "job_id": job.id}