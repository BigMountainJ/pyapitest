import logging
import pickle
import uuid
import os
import numpy as np
from io import BytesIO
from .exceptions import InputFileProcessingException

logger = logging.getLogger(__name__)

def process_csv(file):
  filename = str(uuid.uuid4()) + '.csv'
  file_path = os.path.join('tmp', filename)
  
  if not os.path.exists(file_path):
    file.seek(0)
    file.save(file_path)

  try:
    X_te= np.genfromtxt(file_path, delimiter=',')
    with open('model.pickle', 'rb') as f:
        net,scaler = pickle.load(f) 
    test_preds = net.predict(np.hstack([scaler.transform(X_te[:,:8]),X_te[:,8:]]))
    # Generate output
    output = BytesIO()
    np.savetxt(output, test_preds, delimiter=",")
    output.seek(0)
    return output
  except Exception as err:
    logger.error(err)
    raise InputFileProcessingException("Failed to process the input file")
  finally:
    os.remove(file_path)

