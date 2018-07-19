from app import db

class Service(db.Model):
	__tablename__ = 'services'

	id = db.Column(db.Integer, primary_key = True)
	hh_rel = db.Column(db.Integer)
	xaa_rel = db.Column(db.Integer)
	xaa_nm = db.Column(db.String(128))
	svc_id = db.Column(db.Integer)
	svc_desc = db.Column(db.String(128))
	price_method_curr = db.Column(db.String(10))
	flat_price_curr = db.Column(db.Float)
	tier_price_1_curr = db.Column(db.Float)
	tier_threshold_1_curr = db.Column(db.Integer)
	tier_price_2_curr = db.Column(db.Float)
	tier_threshold_2_curr = db.Column(db.Integer)
	tier_price_3_curr = db.Column(db.Float)
	tier_threshold_3_curr = db.Column(db.Integer)
	tier_price_4_curr = db.Column(db.Float)
	tier_threshold_4_curr = db.Column(db.Integer)
	price_method_new = db.Column(db.String(10))
	flat_price_new = db.Column(db.Float)
	tier_price_1_new = db.Column(db.Float)
	tier_threshold_1_new = db.Column(db.Integer)
	tier_price_2_new = db.Column(db.Float)
	tier_threshold_2_new = db.Column(db.Integer)
	tier_price_3_new = db.Column(db.Float)
	tier_threshold_3_new = db.Column(db.Integer)
	tier_price_4_new = db.Column(db.Float)
	tier_threshold_4_new = db.Column(db.Integer)
	price_method_tmc = db.Column(db.String(10))
	flat_price_tmc = db.Column(db.Float)
	tier_price_1_tmc = db.Column(db.Float)
	tier_threshold_1_tmc = db.Column(db.Integer)
	tier_price_2_tmc = db.Column(db.Float)
	tier_threshold_2_tmc = db.Column(db.Integer)
	tier_price_3_tmc = db.Column(db.Float)
	tier_threshold_3_tmc = db.Column(db.Integer)
	tier_price_4_tmc = db.Column(db.Float)
	tier_threshold_4_tmc = db.Column(db.Integer)

	def __init__(self, hh_rel, xaa_rel, xaa_nm, svc_id, svc_desc, price_method_curr,\
		flat_price_curr, tier_price_1_curr, tier_threshold_1_curr, tier_price_2_curr, \
		tier_threshold_2_curr, tier_price_3_curr, tier_threshold_3_curr,tier_price_4_curr, \
		tier_threshold_4_curr):
		self.hh_rel = hh_rel
		self.xaa_rel = xaa_rel
		self.xaa_nm = xaa_nm
		self.svc_id = svc_id
		self.svc_desc = svc_desc
		self.price_method_curr = price_method_curr
		self.flat_price_curr = flat_price_curr
		self.tier_price_1_curr = tier_price_1_curr
		self.tier_threshold_1_curr = tier_threshold_1_curr
		self.tier_price_2_curr = tier_price_2_curr
		self.tier_threshold_2_curr = tier_threshold_2_curr
		self.tier_price_3_curr = tier_price_3_curr
		self.tier_threshold_3_curr = tier_threshold_3_curr
		self.tier_price_4_curr = tier_price_4_curr
		self.tier_threshold_4_curr = tier_threshold_4_curr
		self.price_method_new = price_method_curr
		self.flat_price_new = flat_price_curr
		self.tier_price_1_new = tier_price_1_curr
		self.tier_threshold_1_new = tier_threshold_1_curr
		self.tier_price_2_new = tier_price_2_curr
		self.tier_threshold_2_new = tier_threshold_2_curr
		self.tier_price_3_new = tier_price_3_curr
		self.tier_threshold_3_new = tier_threshold_3_curr
		self.tier_price_4_new = tier_price_4_curr
		self.tier_threshold_4_new = tier_threshold_4_curr
		self.price_method_tmc = price_method_curr
		self.flat_price_tmc = flat_price_curr
		self.tier_price_1_tmc = tier_price_1_curr
		self.tier_threshold_1_tmc = tier_threshold_1_curr
		self.tier_price_2_tmc = tier_price_2_curr
		self.tier_threshold_2_tmc = tier_threshold_2_curr
		self.tier_price_3_tmc = tier_price_3_curr
		self.tier_threshold_3_tmc = tier_threshold_3_curr
		self.tier_price_4_tmc = tier_price_4_curr
		self.tier_threshold_4_tmc = tier_threshold_4_curr

	@property
	def serialize(self):
		return {
		'name' : self.xaa_nm,
		'desc' : self.svc_desc
		}
	
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

