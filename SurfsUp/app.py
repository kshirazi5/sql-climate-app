import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask,jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(autoload_with=engine)

measurement = Base.classes.measurement
station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route('/')
def Home():
    return ('/')

@app.route('/api/v1.0/precipitation')
def Precitipation():
    previousYear = dt.date(2017,8,23)-dt.timedelta(days=365)
    Results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= previousYear).all()
    Results = {date:prcp for date, prcp in precipitation}
    return jsonify(Results)

