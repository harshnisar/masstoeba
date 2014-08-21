from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, FileField
from wtforms.validators import Required, Length

class TextSubmission(Form):
    name = TextField('name', validators = [Required()])
    # text = TextAreaField('text', validators = [Required(), Length(max=150000)])
    text = FileField(u'file')

class PlayGround(Form):
    text = FileField(u'file')
    lang = TextField(u'lang')
    '''Sentence length thresholds follow'''
    max_thresh = IntegerField(u'max_thresh')
    min_thresh = IntegerField(u'min_thresh')
    '''Uncommon words allowed, sentences not matching
     this criteria are scored 0'''
    uncommon_thresh = IntegerField(u'uncommon_thresh')


    '''Weights'''
    weight_iwf = IntegerField(u'weight_iwf', default=1)
    weight_common = IntegerField(u'weight_common', default=1)
    weight_firstchar = IntegerField(u'weight_first', default=1)
    weight_len = IntegerField(u'weight_len', default=1)