import pandas as pd

def load_data(path):
    '''
    Loads csv into Pandas DataFrame
    '''
    return pd.read_csv(path)

def format_axes(plt):
    '''
    Formats plot axes
    '''
    plt.rcParams['axes.linewidth'] = 3
    plt.rcParams['xtick.major.width'] = 2
    plt.rcParams['ytick.major.width'] = 2
    plt.rcParams['xtick.minor.width'] = 2
    plt.rcParams['ytick.minor.width'] = 2
    plt.rc('xtick.major', size=8, pad=8)
    plt.rc('xtick.minor', size=6, pad=5)
    plt.rc('ytick.major', size=8, pad=8)
    plt.rc('ytick.minor', size=6, pad=5)
    return plt