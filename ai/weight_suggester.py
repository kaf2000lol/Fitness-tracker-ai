from strength_model import predict_next


def suggest(exercise):

    pred = predict_next(exercise)

    return round(pred + 5, 1)
