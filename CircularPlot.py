import matplotlib.pyplot as plt
import numpy as np

def circularPlot(x, y, xmax, ymax, color = "black", lw = 1, grid = True, 
                 yticks = [], num_xticks = 8, xlabels = True, ytitle = None):
    
    # Set limits
    lim = ymax*1.5
    plt.ylim(-lim, lim)
    plt.xlim(-lim, lim)
    
    # Add gridlines
    if grid == True:
        angles = np.linspace(0, np.pi-np.pi/num_xticks*2, int(num_xticks/2))
        for angle in angles:
            xangle = [-1.1*ymax*np.cos(angle),1.1*ymax*np.cos(angle)]
            yangle = [-1.1*ymax*np.sin(angle),1.1*ymax*np.sin(angle)]
            plt.plot(xangle,yangle, "--", color = "gray", lw = 0.8)
            if xlabels != False:
                label_x = 1.2*ymax*np.cos(angle)
                label_y = 1.2*ymax*np.sin(angle)
                plt.annotate("{:.2}".format(angle*xmax/(2*np.pi)), 
                             (label_x, label_y), size = 12, ha='center', va='center')
                if round(angle, 4) != round(np.pi/2, 4) or ytitle == None:
                    plt.annotate("{:.2}".format((angle+np.pi/2)*xmax/(2*np.pi)), 
                             (-label_x, -label_y), size = 12, ha='center', va='center')
        
        # "max" circle
        yticks.append(ymax)
        grid_theta = np.linspace(0, 2*np.pi, 200)
        for tick in yticks:
            x_tick = tick*np.cos(grid_theta)
            y_tick = tick*np.sin(grid_theta)
            plt.plot(x_tick, y_tick, "-", color = "gray", lw = 1.2)
            plt.annotate(tick, (0, -tick -0.07*ymax), ha='center', size = 12)
    
    if ytitle != None:
        plt.annotate(ytitle, (0, -1.2*ymax), size = 14, 
                     ha='center', va='center')
    
    theta = x/xmax*2*np.pi
    
    x_circ = y*np.cos(theta)
    y_circ = y*np.sin(theta)
    
    plt.plot(x_circ, y_circ, color = color, lw = lw)
    plt.xticks([])
    plt.yticks([])
    
def circularDatePlot(dates, y, ymax, color = "black",lw = 1, 
                     yticks = [], ytitle = None, grid = True):
    x = np.asarray([date.year + date.month/12 + date.day/365 for date in dates])
    
    circularPlot(x, y, 1, ymax, color = color, lw = lw, 
                 grid = grid, num_xticks = 12, 
                 xlabels = False, yticks = yticks)
    
    # Add month labels
    if grid == True:
        months = ["Jan", "Feb", "Mar", "Apr","May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
        month_angles = np.linspace(np.pi/12, 2*np.pi-np.pi/12, 12)
        for i, month in enumerate(months):
            month_x = ymax*1.2*np.cos(month_angles[i])
            month_y = ymax*1.2*np.sin(month_angles[i])
            rotation = month_angles[i]/(2*np.pi)*360
            if rotation > 90 and rotation < 270:
                rotation -= 180
            plt.annotate(month, (month_x, month_y),
                         rotation = rotation,
                         ha='center', va='center', size = 12)