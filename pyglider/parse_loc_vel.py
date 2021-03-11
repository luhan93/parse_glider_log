""" parse_loc_vel.py Retrieve gos locations and water velocities for Modena deployment

    Usage: python parse_loc_vel.py Modena

    Inputs:
     glidername modena

     Input path for logs:
     /Users/luhan/Documents/OneDrive - University of North Carolina at Chapel Hill/2018/peach/slocum_glider_data/level0/modena/2018_03/logs

     Output path for kml:
     /Users/luhan/Documents/OneDrive - University of North Carolina at Chapel Hill/2018/peach/slocum_glider_data/level1


"""
import os.path
import sys
import pyglider
import glob
import pandas as pd

if __name__ == '__main__':
    glider = 'modena'
    # fn = '/var/spool/mail/localuser'
    indir = '/Users/luhan/Documents/OneDrive - University of North Carolina at Chapel Hill/2018/peach/slocum_glider_data/level0/modena/2018_03/logs'
    try:
        # lines = pyglider.load_data(fn)
        lines = pyglider.load_glider_logs(indir)
        data1 = pyglider.parse_log_loc_vel(lines, glider)
        # kml = pyglider.generate_track_kml(data1, glider)
        # ofn = '/home/localuser/realtime/tracks/' + glider + '_track.kml'
        # f = open(ofn, 'w')
        # f.write(kml)
        # f.close()
        #
        # debug = 0
        # if debug:
        #     for d in data1:
        #         print
        #         "something"
        #         coord_str = "";
        #         if d['lat'] and d['lon']:
        #             coord_str = coord_str + "%f,%f" % (d['lon'], d['lat'])
        #         print
        #         d['dt_str'], d['gps_dt_str'], coord_str
        #
        df = pd.DataFrame(data1)
        df.to_csv("../loc_vel/loc_vel.csv")


    except:
        print
        "Unexpected error:", sys.exc_info()[0]
        raise
