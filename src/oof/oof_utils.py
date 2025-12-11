def save_oof(oof_array, path):
    import numpy as np
    np.save(path, oof_array)