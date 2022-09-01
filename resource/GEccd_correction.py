import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.image as mpimage
import time
# coding: utf-8
import csv
from scipy import interpolate

info = {}
info['element'] = 'C'
info['energy'] = 445


def fastinterp1(x, y, xi):
    ixi = np.digitize(xi, x)
    n = len(x)
    ixi[ixi == n] = n - 1
    t = (xi - x[ixi - 1]) / (x[ixi] - x[ixi - 1])
    yi = (1 - t) * y[ixi - 1] + t * y[ixi]
    yi = yi.T
    return yi


def detectorclean(exp, noise1, noise2, thresholdUP=0.9, thresholdDOWN=0.1):
    exp = exp - np.mean(exp[:, noise1:noise2])
    exp[exp > (np.max(exp) * thresholdUP)] = 0
    exp[exp < (np.min(exp) * thresholdDOWN)] = 0
    detectorcleanout = exp
    return detectorcleanout


def clear_bg(exp):
    u, v = exp.shape
    temp = np.zeros((u, v))
    for i in np.arange(u):
        k = (np.sum(exp[i, 1:10]) - np.sum(exp[i, -10:-1])) / (v) / 10
        b = np.sum(exp[i, 1:10]) / 10 - k * 10
        exp_bg = -k * np.arange(v) + b
        temp[i, :] = exp[i, :] - exp_bg
    return u, v, temp


def xcorr(x, y, maxlags=10):
    Nx = len(x)
    if Nx != len(y):
        raise ValueError('x and y must be equal length')
    c = np.correlate(x, y, mode=2)

    if maxlags is None:
        maxlags = Nx - 1

    if maxlags >= Nx or maxlags < 1:
        raise ValueError('maxlags must be None or strictly positive < %d' % Nx)

    c = c[Nx - 1 - maxlags:Nx + maxlags]
    lag = np.linspace(-maxlags, maxlags, 2 * maxlags + 1)

    return c, lag


def calculate_line_width(matrix):
    """ # Background subtraction
    ExposureTime = 600 #seconds
    background_aqn_time = 600 #seconds
    extract_background=True
    if extract_background:
        rawImageData = 1. * matrix
        if background.shape == matrix.shape[:2]:
            if background_aqn_time:
                matrix -= np.array(ExposureTime) * background \
                    / background_aqn_time """
    matrix1 = matrix.T

    matrix1 = detectorclean(matrix1, noise1=150, noise2=200)
    m, n, out = clear_bg(matrix1)
    new_img = np.zeros((m, n))
    matrix2 = out
    j = 6
    k = 0.4 + j * 0.1 + j ** 2 * (1e-07)
    low_lim = 1400
    high_lim = 3000
    new_X = np.arange(low_lim, high_lim)
    result = np.zeros(len(new_X))
    xinitial = np.arange(n)
    xinterp = np.arange(0, n, 0.05)
    xx = np.linspace(0, len(xinterp), n)
    for ii in range(m):
        temp = matrix2[ii, :]
        ntemp = fastinterp1(xinitial, temp, xinterp)
        dd = round(k * ii)
        new_img[ii, :] = fastinterp1(new_X, ntemp[low_lim - dd:high_lim - dd], xx)
        # f=interpolate.interp1d(new_X,ntemp[low_lim-dd:high_lim-dd],kind='slinear')
        # new_img = f(xx)
        result = result + ntemp[low_lim - dd:high_lim - dd]

    y_ = fastinterp1(new_X, result, xx)
    x_out = xinitial[round(low_lim / 20):round(high_lim / 20)]
    y_out = y_[round(low_lim / 20):round(high_lim / 20)]
    fileout = np.array([x_out, y_out]).T
    # plt.plot(xinitial[round(low_lim / 20):round(high_lim / 20)],
    #          y_[round(low_lim / 20):round(high_lim / 20)])
    # plt.pause(0.5)
    # plt.show()
    return fileout,x_out,y_out


if __name__ == "__main__":
    # ---------------------------------------------------#
    # thresholdUP = 0.9
    # thresholdDOWN = 0.1
    root = Tk()
    root.withdraw()
    root.update()
    img_path = askopenfilename(title=u'Read CCD image')
    # bg_path = askopenfilename(title=u'Read background image')
    root.destroy()
    matrix = mpimage.imread(img_path).astype('float64')
    # background = mpimage.imread(bg_path).astype('float64')
    fileout,x_out,y_out = calculate_line_width(matrix)
    root = Tk()
    root.withdraw()
    fname = tkinter.filedialog.asksaveasfilename(title=u'保存文件', filetypes=[("csv", ".CSV")])
    fname = fname
    csvfile = open(fname, 'w', newline="")
    writer = csv.writer(csvfile)
    writer.writerow(['pixels', 'intensity'])
    data2 = fileout
    writer.writerows(data2)
    csvfile.close()
