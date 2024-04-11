from acppred.predict import predict_anticancer_peptide


def test_predict_anticancer_peptide():
    predict_anticancer_peptide('AAAAAAA')

def test_predict_anticancer_peptide_variable_type():
    prediction = predict_anticancer_peptide('AAAAAA')
    assert isinstance(prediction, float)