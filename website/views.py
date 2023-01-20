from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from datetime import datetime
from .models import Person, Company, PartCapital
from . import db
import json
from sqlalchemy import or_
from sqlalchemy.ext.serializer import loads, dumps
from sqlalchemy.orm import joinedload

views = Blueprint('views', __name__)

maxDay = datetime.now()

@views.route('/', methods=['GET', 'POST'])
def home():
    companies = db.session.query(Company)
    if request.method == 'POST':
        global selectedCompany
        selectedCompany = request.form.get('idNumber')
        return redirect(url_for('views.view'))
    return render_template("home.html", homepage=True, companies = companies)

@views.route('/osayhingu-andmete-vaade', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        global selectedCompany
        selectedCompany = request.form.get('idNumber')
        return redirect(url_for('views.update'))
    company = Company.query.filter_by(companyId = selectedCompany).first()
    return render_template("view.html", company = company)

# @views.route('/search', methods=['GET', 'POST'])
# def search():
#     suitable = request.form.get('searchText')
#     search = "%{}%".format(suitable)
#     result = Company.query.join(Person, Company.shareOwner).filter(
#             or_(
#                 Company.companyName.like(search),
#                 Company.regCode.like(search),
#                 Person.regCode.like(search),
#                 Person.name.like(search),
#                 Person.firstName.like(search),
#                 Person.lastName.like(search),
#                 Person.personalCode.like(search)
#             )
#     ).all()
#     print(str(Company.query.options(joinedload('shareOwner'))))
#     #result = db.session.query(Company, PartCapital, Person). \
#     #        select_from(Company).join(PartCapital).join(Person).filter(
#     #        or_(
#     #            Company.name.like(search),
#     #            Company.regCode.like(search),
#     #            Person.regCode.like(search),
#     #            Person.name.like(search),
#     #            Person.firstName.like(search),
#     #            Person.lastName.like(search),
#     #            Person.personalCode.like(search)
#     #        )
#     #).all()
#     print(result)
#     companySchema = CompanySchema(many=True)
#     personSchema = PartCapitalSchema(many=True)
#     return jsonify(companySchema.dump(result))

#company.shareOwner.owner.firstName

@views.route('/osayhingu-asutamise-vorm', methods=['GET', 'POST'])
def create():
    persons = db.session.query(Person)

    if request.method == 'POST':
        name = request.form.get('name')
        reg = request.form.get('reg')
        date = request.form.get('date')
        capital = request.form.get('capital')
        selectedPersonsId = request.form.get('selectedPersonsId')
        shareInCompany = request.form.get('shareInCompany')
        checkCompany = Company.query.filter_by(regCode = reg).first()
        if len(name) <= 3 or len(name) > 100 or not all(chr.isalnum() or chr.isspace() for chr in name):
            flash('Nimi peab olema 3 kuni 100 tähte või numbrit', category="error")
        elif len(reg) < 7 or not reg.isnumeric():
            flash('Registrikood peab olema 7 numbrit', category="error")
        elif checkCompany:
            flash('Sama registrikoodiga osaühing on juba olemas', category="error")
        elif (int(capital) < 2500):
            flash('Kogukapitali suurus peab olema vähemalt 2500', category="error")
        elif not date:
            flash('Asutamispäev peab olema valitud', category="error")
        else:
            new_company = Company(companyName = name, regCode = reg, date = datetime.strptime(date, '%Y-%m-%d'), capital = capital)
            idList = selectedPersonsId.split(", ")
            shareList = shareInCompany.split(", ")
            for i in range(len(idList)):
                founder = PartCapital(personIdentifier = idList[i], personShare = shareList[i], personIsFounder = 1)
                founder.person = Person()
                new_company.shareOwner.append(founder)
            db.session.add(new_company)
            db.session.commit()
            global selectedCompany
            selectedCompany = Company.query.filter_by(regCode = reg).first().companyId
            return redirect(url_for('views.view'))
    return render_template("create.html", date=maxDay.strftime('%Y-%m-%d'), persons=persons)

@views.route('/osayhingu-osakapitali-suurendamise-vorm', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        change = request.form.get('idNumber')
        both = change.split(",")
        company = both[0]
        person = both[1]
        money = both[2]
        temp = PartCapital.query.filter_by(companyIdentifier = int(company), personIdentifier = person).first()
        currentCompany = Company.query.filter_by(companyId = int(company)).first()
        currentCompany.capital += int(money)
        if temp:
            temp.personShare += int(money)
            db.session.commit()
        else:
            founder = PartCapital(personIdentifier = person, personShare = money, personIsFounder = 0)
            founder.person = Person()
            currentCompany.shareOwner.append(founder)
            db.session.commit()
    company = Company.query.filter_by(companyId = selectedCompany).first()
    persons = db.session.query(Person)
    return render_template("update.html", company = company, persons = persons)
