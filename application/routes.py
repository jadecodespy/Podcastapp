from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Topics, Podcast
from application.forms import Addtopics, Addpodcast
import requests




@app.route('/')
@app.route('/home', methods = ["GET"])
def home():
    machine = getenv("HOSTNAME")
    podcasts = Podcast.query.order_by(Podcast.title).all()
    return render_template('home.html', title='Home', machine= machine, podcasts=podcasts)


@app.route('/topics', methods= ['GET', 'POST'])
def topics():
    form = Addtopics()
    if form.validate_on_submit():
        topics = Topics(
                title = form.title.data,
                description = form.description.data
        )
        db.session.add(topics)
        db.commit()
        return redirect(url_for('home'))
    else:
        print (forms.errors)
        
    return render_template('topics.html', title='Enter a Topic', form = form)


@app.route('/podcast', methods= ['GET', 'POST'])
def podcast():
    form = Addpodcast()
    if form.validate_in_submit():
        podcast = Podcast(
                title = form.title.data,
                detail = form.detail.data,
        )

        if form.topic_one.data!= '':
            topic_one = Topics.query.filter_by(title = form.topic_one.data).first()
            if topic_one:
                podcast.episode.append(topic_one)
        db.session.add(podcast)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)


    return render_template('podcast.html', title='Enter Podcast', form = form)


@app.route('/schedule')
def schedule():
    return render_template('schedule.html', title='schedule', desc='Scheduling Page')                                                                                  
