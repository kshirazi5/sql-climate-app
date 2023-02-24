import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask,jsonify
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(autoload_with=engine)

Measurement = Base.classes.measurement
Station = Base.classes.station


app = Flask(__name__)

@app.route('/')
def Home():
    routes = (f"/<br>"
        f"/api/v1.0/precipitation<br>"
       f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
         f"/api/v1.0/temp/&lt;start&gt;<br>"
        f"/api/v1.0/temp/&lt;start&gt;/&lt;end&gt;<br>" 
    )
    return (routes)

@app.route('/api/v1.0/precipitation')
def Precipitation():
    session = Session(engine)
    previous_year = dt.date(2017,8,23)-dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= previous_year).all()
    values = {date:prcp for date, prcp in results}
    session.close()
    return jsonify(values)


@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)

    get_stations=session.query(Station.station).all()
    list_stations=list(np.ravel(get_stations))

    session.close()
    
    return jsonify(list_stations)


@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)

    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d')
    query_dt = dt.date(recent_date.year -1, recent_date.month, recent_date.day)

    all_tobs=session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= query_dt).all()
    temp_Observe=[]
    for date, tobs in all_tobs:
        dtobs={}
        dtobs["date"]=date
        dtobs["tobs"]=tobs

        temp_Observe.append(dtobs)
    session.close()

    return jsonify(temp_Observe)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    session = Session(engine)

    """Return TMIN, TAVG, TMAX."""
    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:   
        start = dt.datetime.strptime(start, "%m%d%Y")
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        session.close()
        temps = list(np.ravel(results))
        return jsonify(temps)
    # calculate TMIN, TAVG, TMAX with start and stop
    start = dt.datetime.strptime(start, "%m%d%Y")
    end = dt.datetime.strptime(end, "%m%d%Y")
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    session.close()
    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


if __name__ == '__main__':
    app.run()