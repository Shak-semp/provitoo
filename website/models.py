from . import db
#from marshmallow import fields

class PartCapital(db.Model):
    __tablename__ = "part_capital_table"
    personIdentifier = db.Column('person_id', db.Integer, db.ForeignKey('person_table.id'), primary_key=True)
    companyIdentifier = db.Column('company_id', db.Integer, db.ForeignKey('company_table.companyId'), primary_key=True)
    personShare = db.Column('person_share', db.Integer)
    personIsFounder = db.Column('person_is_founder', db.Integer)
    owner = db.relationship("Person", back_populates="shareCompany")
    company = db.relationship("Company", back_populates="shareOwner")

class Company(db.Model):
    __tablename__ = "company_table"
    companyId = db.Column(db.Integer, primary_key=True)
    companyName = db.Column(db.String(101))
    regCode = db.Column(db.Integer, unique=True)
    date = db.Column(db.Date())
    capital = db.Column(db.Integer)
    shareOwner = db.relationship('PartCapital', back_populates="company")

class Person(db.Model):
    __tablename__ = "person_table"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer(), nullable=False)
    firstName = db.Column(db.String(250), nullable=True)
    lastName = db.Column(db.String(250), nullable=True)
    personalCode = db.Column(db.String(15), nullable=True, unique=True)
    name = db.Column(db.String(250), nullable=True)
    regCode = db.Column(db.String(250), nullable=True, unique=True)
    shareCompany = db.relationship('PartCapital', back_populates="owner")

# class PersonSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Person
        

# class CompanySchema(ma.SQLAlchemyAutoSchema):
#     shareOwner = fields.Nested(PersonSchema, many=True)
#     class Meta:
#         model = Company

# class PartCapitalSchema(ma.SQLAlchemyAutoSchema):
#     owner = fields.Nested(PersonSchema, many=True)
#     company = fields.Nested(CompanySchema, many=True)
#     class Meta:
#         model = PartCapital
