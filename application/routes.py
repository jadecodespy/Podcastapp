from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Topics, Podcast
from application.forms import Addtopics, Addpodcast, UpdateTopicsForm
import requests
from os import getenv



@app.route('/')
@app.route('/home', methods = ["GET"])
def home():
    machine = getenv("HOSTNAME")
    podcasts = Podcast.query.order_by(Podcast.podcast_title).all()
    return render_template('home.html', title='Home', machine= machine, podcasts=podcasts)


@app.route('/topics', methods= ['GET', 'POST'])
def topics():
    form = Addtopics()
    if form.validate_on_submit():
        topics = Topics(
                topic_title = form.title.data,
                topic_desc = form.description.data
        )
        db.session.add(topics)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print (form.errors)
        
    return render_template('topics.html', title='Enter a Topic', form = form)


@app.route('/podcast', methods= ['GET', 'POST'])
def podcast():
    form = Addpodcast()
    if form.validate_on_submit():
        podcast = Podcast(
                podcast_title = form.title.data,
                podcast_detail = form.detail.data,
        )

        if form.topic_one.data!= '':
            print("if form topic one")
            topic_one = Topics.query.filter_by(topic_title = form.topic_one.data).first()
            if topic_one:
                print("iftopic one")
                podcast.episode.append(topic_one)
        db.session.add(podcast)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)


    return render_template('podcast.html', title='Enter Podcast', form = form)


@app.route('/updatetopics/<int:id>', methods=['GET', 'POST'])
def updatetopics(id):
    form = UpdateTopicsForm()
    topic=Topics.query.filter_by(id = id).first()
    if form.validate_on_submit():
        topic.topic_title = form.title.data
        topic.topic_desc = form.description.data

        db.session.commit()
        return redirect(url_for('home'))
    else:
        form.title.data = topic.topic_title
        form.description.data = topic.topic_desc
    



    return render_template('updatetopic.html', title = 'Update Topic', form = form, topic = topic)





@app.route('/topics/delete/<int:id>', methods = ["GET", "POST"])
def topic_delete(id):
    episode= Topics.query.filter_by(id=id).first()
    db.session.delete(episode)
    db.session.commit()
    return redirect(url_for('home'))








@app.route('/schedule')
def schedule():
    return render_template('schedule.html', title='schedule', desc='Scheduling Page')                                                                                  
