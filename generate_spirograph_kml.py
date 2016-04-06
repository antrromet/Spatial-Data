from __future__ import division
import math

__author__ = "Antrromet"
__email__ = "antrromet@gmail.com"


# R=5, r=1, a=4
# x(t) = (R+r)*cos((r/R)*t) - a*cos((1+r/R)*t)
# y(t) = (R+r)*sin((r/R)*t) - a*sin((1+r/R)*t)

def write_head_kml(kml_file, center_x, center_y):
    kml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    kml_file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    kml_file.write('\t<Document>\n')
    kml_file.write('\t\t<Style id="red">\n')
    kml_file.write('\t\t\t<IconStyle>\n')
    kml_file.write('\t\t\t\t<Icon>\n')
    kml_file.write('\t\t\t\t\t<href>http://www.google.com/intl/en_us/mapfiles/ms/micons/red-dot.png</href>\n')
    kml_file.write('\t\t\t\t</Icon>\n')
    kml_file.write('\t\t\t</IconStyle>\n')
    kml_file.write('\t\t</Style>\n')
    kml_file.write('\n')
    kml_file.write('\t\t<Style id="blue">\n')
    kml_file.write('\t\t\t<IconStyle>\n')
    kml_file.write('\t\t\t\t<Icon>\n')
    kml_file.write('\t\t\t\t\t<href>http://maps.gstatic.com/mapfiles/ridefinder-images/mm_20_blue.png</href>\n')
    kml_file.write('\t\t\t\t</Icon>\n')
    kml_file.write('\t\t\t</IconStyle>\n')
    kml_file.write('\t\t</Style>\n')
    kml_file.write('\n')
    kml_file.write('\t\t<Placemark>\n')
    kml_file.write('\t\t\t<name>SGM124</name>\n')
    kml_file.write('\t\t\t<Point>\n')
    kml_file.write(
        '\t\t\t\t<coordinates>' + str(center_y) + ',' + str(center_x) + '</coordinates>\n')
    kml_file.write('\t\t\t</Point>\n')
    kml_file.write('\t\t\t<styleUrl>#red</styleUrl>\n')
    kml_file.write('\t\t</Placemark>\n')
    kml_file.write('\n')


def write_spiro_points(kml_file, spiro_points, center_x, center_y):
    for i, point in enumerate(spiro_points):
        kml_file.write('\t\t<Placemark>\n')
        kml_file.write('\t\t\t<name></name>\n')
        kml_file.write('\t\t\t<Point>\n')
        kml_file.write(
            '\t\t\t\t<coordinates>' + str(center_y + point[0]) + ',' + str(center_x + point[1]) + '</coordinates>\n')
        kml_file.write('\t\t\t</Point>\n')
        kml_file.write('\t\t\t<styleUrl>#blue</styleUrl>\n')
        kml_file.write('\t\t</Placemark>\n')
        kml_file.write('\n')


def write_tail_kml(kml_file):
    kml_file.write('\t</Document>\n')
    kml_file.write('</kml>')


def compute_spiro_values(R, r, a):
    points = []
    t = 0.0
    while t <= 50.0:
        x = (R + r) * math.cos((r / R) * t) - a * math.cos((1 + r / R) * t)
        y = (R + r) * math.sin((r / R) * t) - a * math.sin((1 + r / R) * t)
        t += 0.01
        points.append((x, y))
        # print str(t) + ': ' + str(y) + "," + str(x)
    return points


def main():
    R = 5
    r = 1
    a = 4
    # SGM Cordinates
    center_x = 34.020360
    center_y = -118.287706
    kml_file = open('spiro.kml', 'w+')
    write_head_kml(kml_file, center_x, center_y)
    spiro_points = compute_spiro_values(R, r, a)
    write_spiro_points(kml_file, spiro_points, center_x, center_y)
    write_tail_kml(kml_file)
    pass


if __name__ == '__main__':
    main()
