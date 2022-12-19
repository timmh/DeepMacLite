import os
import tensorflow as tf

# Convert the model
model = tf.keras.models.load_model(os.path.join("weights", "deepmac_1024x1024_coco17", "saved_model"))
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
converter._experimental_lower_tensor_list_ops = False
tflite_model = converter.convert()

# Save the model.
with open(os.path.join("weights", "deepmac_1024x1024_coco17.tflite"), "wb") as f:
    f.write(tflite_model)