from PIL import Image
import numpy as np
import pprint


def intensity(x,y,img):
        r,g,b=img.getpixel((x,y))
        intens=r+g+b
        return intens

def draw_lines_in_bulk(threshold,num_vert,num_hor,jump,img):                                            
        print('draw_lines_in_bulk(',threshold,',',num_vert,',',num_hor,',',jump,',',filename,')')
        lines=list()                                                                                    #horizontal lines on bright objects
        centers=list()                                                                                  #centers of those lines
        center_to_line=dict()                                                                           #assign center to the correscponding line
         
        for sq_y in range(num_vert):                                                                    #scanning the image
                line=list()
                for sq_x in range(num_hor):
        
                        x1,y1=jump*sq_x,jump*sq_y                                                       #current point of interest
                        x2,y2=x1-jump,y1                                                                #predecessor
                        intens1=intensity(x1,y1,img)
                        intens2=intensity(x2,y2,img)

                        if intens1>threshold:                                                           #lines in 'Bulk' of the object
                                line.append((x1,y1))
                        if intens1-intens2<0 and abs(intens1-intens2)>threshold and len(line)>1:        #determines the centers of horizontal lines
                                start,end=line[0],line[-1]
                                distance=abs(start[0]-end[0])
                                center=(int(x1-distance/2),y1)
                                centers.append(center)
                                center_to_line[center]=line
                                lines.append((len(line),line))
                                line=list()
        return (centers,lines,center_to_line)

def group_points(pointlist,tolerance):                                                                  #assigns points to circle           
        print('group_points(',len(pointlist),',',tolerance,')')
        groups=[]
        i=0
        for a,b in pointlist:
                i=i+1
                group_found = None
                for group in groups:
                        for a1,b1 in group:
                                distance=abs(int(((a-a1)**2+(b-b1)**2)**0.5))
                                if distance<=tolerance:
                                        group_found = group
                                        break
                        if group_found:
                                break
                if group_found:
                        group.append((a,b))
                else:
                        groups.append([(a,b)])                                                                  #Pearl_chain
        pearl_chain=[gr for gr in groups if len(gr)>1]                                                        #remove small groups, as they might be artefacts
        
        
        bulk=list()
        for group in pearl_chain:
                line_group=list()
                for center in group:
                        line=center_to_line[center]
                        for point in line:
                                line_group.append(point)
                bulk.append(line_group)


        print('number of circular objects',len(pearl_chain))
        
        return (pearl_chain,bulk)


def centers_and_radii(pearl_chain,jump):
        circles_dict=dict()
        centers_list=list()
        for group in pearl_chain:
                radius=int(len(group)*jump/2)
                sorted_by_y = sorted(group, key=lambda tup: tup[1])
                top_point=sorted_by_y[0][1]
                center=(group[0][0],int(top_point+radius))
                circles_dict[center]=radius
                centers_list.append([center])
        pprint.pprint(circles_dict)
        return (circles_dict,centers_list)
                
                
                
                


def Show_groups(grouped_list,img,name, magni):
        
        red,green,blue,yellow = (255,0,0),(0,255,0),(0,0,255),(255,255,0)
        colorlist=[yellow,green,red,blue]*100
        c=0
        
        for group in grouped_list:
                for x,y in group:
                        for xx in range(-magni*int(jump/2),magni*int(jump/2)):
                                for yy in range(-magni*int(jump/2),magni*int(jump/2)):
                                        img.putpixel((x+xx,y+yy),colorlist[c])
                c=c+1
        new_name='output'+'_'+filename+'_'+name+'.jpg'
        img.save(new_name) 

#############################################################################
################ Execute####################################################
############################################################################


filename= '2_overlapping_circles'   # also try '1_single_circles'
file=filename+'.jpg'
img=Image.open(file).convert('RGB')
width = img.size[0]
height = img.size[1]


jump=5    
nx=int(width/jump)
ny=int(height/jump)
th=200

(centers,lines,center_to_line)=draw_lines_in_bulk(th,ny,nx,jump,img)
(pearl_chain,bulk)=group_points(centers,jump*2)
(circles_dict,centers_list)=centers_and_radii(pearl_chain,jump)
Show_groups(centers_list,img,'centers',5)
Show_groups(pearl_chain,img,'pearlchain',2)
Show_groups(bulk,img,'bulk',1)

        

