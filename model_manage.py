from codes.config import *
from codes.util.util_dir import *
from codes.util.util_log import logger
from codes.model.model_pbycyc import *
from codes.model.model_pbycyy import *
import warnings
from datetime import datetime

warnings.filterwarnings(action='ignore', category=DeprecationWarning)  # ¹ËÂÇ¾¯¸æ


def model_control_mark(db_engine, model=''):
    if model == 'pbycyy':
        sql = '''SELECT MAX(DATA_DATE) FROM T_PBYCYY_DATA_COMBINE '''
    elif model == 'pbycyc':
        sql = '''SELECT MAX(DATA_DATE) FROM T_PBYCYC_DATA_COMBINE_WEEK '''
    else:
        pass

    maxdate_pbyc = pd.read_sql(sql, con=db_engine).values[0][0]
    maxdate_pbyc = datetime.date(datetime.strptime(maxdate_pbyc, "%Y-%m-%d %H:%M:%S"))
    sys_date = datetime.date(datetime.now())
    pbyc_timedelta = (sys_date - maxdate_pbyc).days
    if pbyc_timedelta == 1:
        return 1
    else:
        return 0
