from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from . models import Home,About, Portfolio,News,Contact,Admin
from Project import app, db, os,bcrypt,login_manager
from . forms import ContactForm ,Adminlogin
from flask_login import login_user,login_required,logout_user



@app.route('/')
@app.route('/home')
def home():
    home=Home.query.all()
    return render_template('home.html',home=home)

@app.route('/about')
def about():
    about = About.query.all()
    return render_template('about.html',about=about)


@app.route('/portfolio')
def portfolio():
    portfolio = Portfolio.query.all()
    return render_template('portfolio.html',portfolio=portfolio)



@app.route('/news')
def news():
    news=News.query.all()
    return render_template('news.html',news=news)



########################################Home################################################################
@app.route('/admin/add-home', methods=['GET', 'POST'])
@login_required
def add_home():
    if request.method == 'POST':   
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        homedata=Home(
            name=request.form.get('name'),
            text=request.form.get('text'),
            fb=request.form.get('fb'),
            insta=request.form.get('insta'),
            twitter=request.form.get('twitter'),
            image = filename
 
        )
        db.session.add(homedata)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('admin/add-home.html')


@app.route('/admin/home-list')
@login_required
def admin_home_list():
    home = Home.query.all()
    return render_template('admin/home-list.html', home=home)


@app.route('/admin/edit-home/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit_home(id):
    homedata = Home.query.get_or_404(id)
    if request.method == 'POST':
        

        homedata.name=request.form.get('name')
        homedata.text=request.form.get('text')
        homedata.fb=request.form.get('fb')
        homedata.insta=request.form.get('insta')
        homedata.twitter=request.form.get('twitter')

      
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('admin/edit-home.html', homedata=homedata)

@app.route('/admin/delete-home/<int:id>', methods=['GET','POST'])
@login_required
def delete_home(id):
    homedata = Home.query.get_or_404(id)
    db.session.delete(homedata)
    db.session.commit()
    return redirect(url_for('home'))


########################################About################################################################
@app.route('/admin/add-about', methods=['GET', 'POST'])
@login_required
def add_about():
    if request.method == 'POST':   
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        aboutdata=About(
            text=request.form.get('text'),
            image = filename
 
        )
        db.session.add(aboutdata)
        db.session.commit()
        return redirect(url_for('about'))
    return render_template('admin/add-about.html')


@app.route('/admin/about-list')
@login_required
def admin_about_list():
    about = About.query.all()
    return render_template('admin/about-list.html', about=about)


@app.route('/admin/edit-about/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit_about(id):
    aboutdata = About.query.get_or_404(id)
    if request.method == 'POST':
        
        aboutdata.text = request.form.get('text')
        
        db.session.commit()

        return redirect(url_for('about'))
    return render_template('admin/edit-about.html', aboutdata=aboutdata)

@app.route('/admin/delete-about/<int:id>', methods=['GET','POST'])
@login_required
def delete_about(id):
    aboutdata = About.query.get_or_404(id)
    db.session.delete(aboutdata)
    db.session.commit()
    return redirect(url_for('about'))

##########################################Portfolio#########################################################

@app.route('/admin/add-portfolio', methods=['GET', 'POST'])
@login_required
def add_portfolio():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        portdata=Portfolio(
            title = request.form.get('title'),
            link = request.form.get('link'),
            image = filename
        )
        db.session.add(portdata)
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/add-portfolio.html')


@app.route('/admin/portfolio-list')
@login_required
def admin_portfolio_list():
    portfolio = Portfolio.query.all()
    return render_template('admin/portfolio-list.html', portfolio=portfolio)


@app.route('/admin/edit-portfolio/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit_portfolio(id):
    portdata = Portfolio.query.get_or_404(id)
    if request.method == 'POST':
        

        portdata.title = request.form.get('title')
        portdata.link = request.form.get('link')
        
        db.session.commit()
        return redirect(url_for('portfolio'))
    return render_template('admin/edit-portfolio.html', portdata=portdata)

@app.route('/admin/delete-portfolio/<int:id>', methods=['GET','POST'])
@login_required
def delete_portfolio(id):
    portdata = Portfolio.query.get_or_404(id)
    db.session.delete(portdata)
    db.session.commit()
    return redirect(url_for('portfolio'))

##########################################NEWS#########################################################

@app.route('/admin/add-news', methods=['GET', 'POST'])
@login_required
def add_news():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))       
        newsdata=News(
            title = request.form.get('title'),
            text=request.form.get('text'),
            image = filename
        )
        db.session.add(newsdata)
        db.session.commit()
        return redirect(url_for('news'))
    return render_template('admin/add-news.html')


@app.route('/admin/news-list')
@login_required
def admin_news_list():
    news = News.query.all()
    return render_template('admin/news-list.html', news=news)


@app.route('/admin/edit-news/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    newsdata = News.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        newsdata.title = request.form.get('title')
        newsdata.text = request.form.get('text')
        newsdata.image = filename


        db.session.commit()
        return redirect(url_for('news'))
    return render_template('admin/edit-news.html', newsdata=newsdata)


@app.route('/admin/delete-news/<int:id>', methods=['GET','POST'])
@login_required
def delete_news(id):
    newsdata = News.query.get_or_404(id)
    db.session.delete(newsdata)
    db.session.commit()
    return redirect(url_for('news'))
###################################CONTACT#######################################################3
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name = form.name.data,
            email = form.email.data,
            message = form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect('contact')
    return render_template('contact.html', form=form)

@app.route('/admin/contact-list')
@login_required
def admin_contact_list():
    form = Contact.query.all()
    return render_template('admin/contact-list.html', form=form)

@app.route('/admin/delete-contact/<int:id>', methods=['GET','POST'])
@login_required
def delete_contact(id):
    form = Contact.query.get_or_404(id)
    db.session.delete(form)
    db.session.commit()
    return redirect(url_for('contact'))


@app.route('/admin',methods=['GET','POST'])
def login():
    form=Adminlogin()
    if form.validate_on_submit():

        user=Admin.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('admin_home_list'))


        return redirect(url_for('login'))

    return render_template('admin/login.html',addata=form)



''' @app.route("/admin/loginadd",methods=['GET','POST'])
@login_required
def loginadd():
    
    form=Adminlogin()
    if form.validate_on_submit():
        user_row_password=form.password.data
        pas_hash=bcrypt.generate_password_hash(user_row_password).decode('utf-8')
        
        user=Admin(
            login=form.login.data,      
            password=pas_hash
        )
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))

    return render_template('admin/admincreatelog.html',form=form) '''