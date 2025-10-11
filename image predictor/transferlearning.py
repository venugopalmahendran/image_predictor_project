import joblib
from pipeline_compontents import Imagepreprocess
from pipeline_compontents import kerasmodelwrapper

model=joblib.load("image_model.joblib")
