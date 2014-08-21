from masstoeba import app
from masstoeba import db

ROLE_USER = 0
ROLE_ADMIN = 1


class eng_orphanage(db.Model):
    '''Used to store all the sentences that are not yet been proofread
    of english language

    '''
    id = db.Column(db.Integer, primary_key = True)
    sentence = db.Column(db.String(200), index = True, unique = False)
    score = db.Column(db.Integer, index = True, unique = False)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    
    '''Crowd Score is the score given by the crowd, if a sentence is
     proofread by enough number of people it can be then finally passed
    on to the main database.
    For testing we could set the min_crowd_score as 1.
    '''
    crowd_score = db.Column(db.Integer, unique = False)
    '''

    Statuses,
    1. Not Taken for edit
    2. Taken for edit
    3. Edited once.

    '''



    status = db.Column(db.SmallInteger, unique = False)

    def __repr__(self):
        # return '<Sentence %r>' % (self.sentence) 
        return self
