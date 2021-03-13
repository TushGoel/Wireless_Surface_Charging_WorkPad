#from keras.models import model_from_json, load_model
#from sklearn.externals import joblib
#
#class modelloader():
#    model_Laptop = None
#    model_M1 = None
#    scalerL = None
#    scalerM = None
#    classesLaptop=None
#    classesM1=None
#    
#    def __init__(self):
#        with open('keras_architectureLaptop1001.json','r') as f:
#            self.model_Laptop = model_from_json(f.read())
#        self.model_Laptop.load_weights('keras_weightsLaptop1001.h5')
#        with open('keras_architectureM.json','r') as f:
#            self.model_M1 = model_from_json(f.read())
#        self.model_M1.load_weights('keras_weightsM.h5')
#        
#    def modelVariables(self):
#         
#        self.scalerL = joblib.load("LaptopScaler1001.pkl")
#        self.scalerM = joblib.load("MobileScaler.pkl")
#        self.classesLaptop=np.loadtxt("LaptopLabels1001.csv",delimiter=',')
#        self.classesM1=np.loadtxt("MobileLabels.csv",delimiter=',')
#        
#        return [self.model_Laptop, self.model_M1, self.scalerL, self.scalerM , self.classesLaptop, self.classesM1]
#        