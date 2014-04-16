from app import celery

@celery.task
def move(directoin,n):
  print "Moving forward %s spaces" % n