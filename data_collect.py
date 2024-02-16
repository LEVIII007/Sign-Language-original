import cv2
import os


directory= 'Sign_img_data/'
print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory)
if not os.path.exists(f'{directory}/blank'):
    os.mkdir(f'{directory}/blank')
if not os.path.exists(f'{directory}/hello'):
    os.mkdir(f'{directory}/hello')
if not os.path.exists(f'{directory}/Namaste'):
    os.mkdir(f'{directory}/Namaste')
if not os.path.exists(f'{directory}/you'):
    os.mkdir(f'{directory}/you')
if not os.path.exists(f'{directory}/love'):
    os.mkdir(f'{directory}/love')
if not os.path.exists(f'{directory}/how_are_you'):
    os.mkdir(f'{directory}/how_are_you')
if not os.path.exists(f'{directory}/good'):
    os.mkdir(f'{directory}/good')
if not os.path.exists(f'{directory}/I_need_help'):
    os.mkdir(f'{directory}/I_need_help')
if not os.path.exists(f'{directory}/Byee'):
    os.mkdir(f'{directory}/Byee')
    

for i in range(65,91):
    letter  = chr(i)
    if not os.path.exists(f'{directory}/{letter}'):
        os.mkdir(f'{directory}/{letter}')




import os
import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/A")),
             'b': len(os.listdir(directory+"/B")),
             'c': len(os.listdir(directory+"/C")),
             'd': len(os.listdir(directory+"/D")),
             'e': len(os.listdir(directory+"/E")),
             'f': len(os.listdir(directory+"/F")),
             'g': len(os.listdir(directory+"/G")),
             'h': len(os.listdir(directory+"/H")),
             'i': len(os.listdir(directory+"/I")),
             'j': len(os.listdir(directory+"/J")),
             'k': len(os.listdir(directory+"/K")),
             'l': len(os.listdir(directory+"/L")),
             'm': len(os.listdir(directory+"/M")),
             'n': len(os.listdir(directory+"/N")),
             'o': len(os.listdir(directory+"/O")),
             'p': len(os.listdir(directory+"/P")),
             'q': len(os.listdir(directory+"/Q")),
             'r': len(os.listdir(directory+"/R")),
             's': len(os.listdir(directory+"/S")),
             't': len(os.listdir(directory+"/T")),
             'u': len(os.listdir(directory+"/U")),
             'v': len(os.listdir(directory+"/V")),
             'w': len(os.listdir(directory+"/W")),
             'x': len(os.listdir(directory+"/X")),
             'y': len(os.listdir(directory+"/Y")),
             'z': len(os.listdir(directory+"/Z")),
             'blank': len(os.listdir(directory+"/blank")),
             'hello': len(os.listdir(directory+"/hello")),
             'love': len(os.listdir(directory+"/love")),
             'you': len(os.listdir(directory+"/you")),
            #  'blank': len(os.listdir(directory+"/blank")),
             'good': len(os.listdir(directory+"/good")),
             'how_are_you': len(os.listdir(directory+"/how_are_you")),
             'Namaste': len(os.listdir(directory+"/Namaste")),
             'I_need_help': len(os.listdir(directory+"/I_need_help")),
             'Byee': len(os.listdir(directory+"/Byee")),
             }

    # row = frame.shape[1]
    # col = frame.shape[0]
    # cv2.rectangle(frame,(0,40),(300,300),(255,255,255),2)
    # cv2.imshow("data",frame)
    # frame=frame[40:300,0:300]
    # cv2.imshow("ROI",frame)
    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # frame = cv2.resize(frame,(48,48))
    frame = cv2.flip(frame, 1)

    # Increase the size of the frame
    frame = cv2.resize(frame, (1200, 1000))

    # Draw a larger rectangle
    cv2.rectangle(frame, (700, 40), (1200, 700), (255, 255, 255), 2)

    # Display the modified frame
    cv2.imshow("data", frame)

    # Extract the region of interest (ROI)
    roi = frame[40:700, 700:1200]

    # Display the ROI
    cv2.imshow("ROI", roi)

    # Convert the ROI to grayscale and resize
    frame = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (80, 80))

# Further processing...

    interrupt = cv2.waitKey(10)
    # if interrupt & 0xFF == ord('a'):
    #     cv2.imwrite(os.path.join(directory+'A/'+str(count['a']))+'.jpg',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(os.path.join(directory+'B/'+str(count['b']))+'.jpg',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(os.path.join(directory+'C/'+str(count['c']))+'.jpg',frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(os.path.join(directory+'D/'+str(count['d']))+'.jpg',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(directory+'E/'+str(count['e']))+'.jpg',frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(os.path.join(directory+'F/'+str(count['f']))+'.jpg',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(os.path.join(directory+'G/'+str(count['g']))+'.jpg',frame)
    # if interrupt & 0xFF == ord('h'):
    #     cv2.imwrite(os.path.join(directory+'H/'+str(count['h']))+'.jpg',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(os.path.join(directory+'I/'+str(count['i']))+'.jpg',frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(os.path.join(directory+'J/'+str(count['j']))+'.jpg',frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(os.path.join(directory+'K/'+str(count['k']))+'.jpg',frame)
    # if interrupt & 0xFF == ord('l'):
    #     cv2.imwrite(os.path.join(directory+'L/'+str(count['l']))+'.jpg',frame)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(os.path.join(directory+'M/'+str(count['m']))+'.jpg',frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(os.path.join(directory+'N/'+str(count['n']))+'.jpg',frame)
    # if interrupt & 0xFF == ord('o'): 
    #     cv2.imwrite(os.path.join(directory+'O/'+str(count['o']))+'.jpg',frame)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(os.path.join(directory+'P/'+str(count['p']))+'.jpg',frame)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(os.path.join(directory+'Q/'+str(count['q']))+'.jpg',frame)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(os.path.join(directory+'R/'+str(count['r']))+'.jpg',frame)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(os.path.join(directory+'S/'+str(count['s']))+'.jpg',frame)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(os.path.join(directory+'T/'+str(count['t']))+'.jpg',frame)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(os.path.join(directory+'U/'+str(count['u']))+'.jpg',frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(os.path.join(directory+'V/'+str(count['v']))+'.jpg',frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(directory+'W/'+str(count['w']))+'.jpg',frame)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(os.path.join(directory+'X/'+str(count['x']))+'.jpg',frame)
    # if interrupt & 0xFF == ord('y'):
    #     cv2.imwrite(os.path.join(directory+'Y/'+str(count['y']))+'.jpg',frame)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(os.path.join(directory+'Z/'+str(count['z']))+'.jpg',frame)
    if interrupt & 0xFF == ord('.'):
        cv2.imwrite(os.path.join(directory+'blank/' + str(count['blank']))+ '.jpg',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(os.path.join(directory+'hello/' + str(count['hello']))+ '.jpg',frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(os.path.join(directory+'you/' + str(count['you']))+ '.jpg',frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(os.path.join(directory+'Byee/' + str(count['Byee']))+ '.jpg',frame)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory+'how_are_you/' + str(count['how_are_you']))+ '.jpg',frame)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(os.path.join(directory+'I_need_help/' + str(count['I_need_help']))+ '.jpg',frame)

    