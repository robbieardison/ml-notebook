import joblib
[...] # import KMeans, BaseEstimator, TransformerMixin, rbf_kernel, etc.
def column_ratio(X): [...]
def ratio_name(function_transformer, feature_names_in): [...] 
class ClusterSimilarity(BaseEstimator, TransformerMixin): [...]
final_model_reloaded = joblib.load("my_california_housing_model.pkl") new_data = [...] # some new districts to make predictions for
predictions = final_model_reloaded.predict(new_data)