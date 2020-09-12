from flask_restful import Resource
import logging as logger

class TaskBYID(Resource):
    
    def get(self,taskid):
        logger.debug("Inside get method of task by id")
        return {"message":"inside get method of task by id. TASK-ID = {}".format(taskid) },200
    
    def post(self,taskid):
        logger.debug("Inside post method of task by id")
        return {"message":"inside post method of task by id. TASK-ID = {}".format(taskid)},200
    
    def put(self,taskid):
        logger.debug("Inside put method of task by id")
        return {"message":"inside put method of task by id. TASK-ID = {}".format(taskid)},200
    
    def delete(self,taskid):
        logger.debug("Inside delete method of task by id")
        return {"message":"inside delete method of task by id. TASK-ID = {}".format(taskid)},200