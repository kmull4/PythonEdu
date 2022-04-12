/*
AHK Script Testing Grounds
https://www.autohotkey.com/docs/commands/WinMove.htm
https://www.autohotkey.com/docs/commands/WinGetPos.htm
https://www.autohotkey.com/docs/commands/SysGet.htm
*/

;~~~~~~~~~~Settings~~~~~~~~~~
SetTitleMatchMode, 2
^F5::Reload
return
+F5::Edit
return

;~~~~~~~~~~I declare these Frycook Games open!~~~~~~~~~~

F3::
; use SysGet to get monitor info and assign variables to these values
SysGet, numMonitors, MonitorCount   ; get num of monitors
SysGet, primMonitor, MonitorPrimary   ; and primary monitor

; make a dictionary supporting up to 4 monitors, can't figure it out for a variable amount
mydict := {mon1:[], mon2:[], mon3:[], mon4:[]}

; for loop to set variables for each monitor
counter := 0    ; need another count in for loop below
for k, v in mydict {
    if (counter == numMonitors) {
    break   ; this is where the other counter comes in
    }
    counter += 1
    SysGet, myOutput, Monitor , %counter%
    v.push(myOutputLeft, myOutputTop, myOutputRight, myOutputBottom)    ; append the array
    MsgBox % k ", " v[3]
}
return


;~~~~~~~~~~
; list of the windows to have on the primary screen

; list of the windows to have on the secondary screen
; or maybe make a dictionary of the windows with format 'program:window,half screen (left or right)'

; move window function. next step is to take in parameters for primary or secondary screens
MoveWindow(WinTitle)
{
    WinGetPos, xpos, ypos, wid, hei, %WinTitle%
    ; AHK msgbox turns everything after comma to str, so need separate variables
    scrWidHalf := (A_ScreenWidth/2), winWidHalf := (wid/2)
    WinMove, %WinTitle%,, 1920, -557, 200, 200
    ; detailed message box of where everything is now
    Msgbox, %WinTitle% at %xpos%`, %ypos% -- %wid% wide %hei% high `nscreenWidth/2 = %scrWidHalf% and winWidHalf = %winWidHalf%
}

; this part will just run in the final version
; loop through what goes to primary screen and what goes to secondary screen
; perhaps with one loop, maybe make dictionary entries and have the definitions be the specifying parameters?


F4::	; AHK, do the thing!
;MoveWindow("ahk_exe Spotify.exe")
myarray := ["asdf","345"]
myarray.Push(6)
MsgBox % myarray[3]
return


^q::	; get info
WinGetPos, xpos, ypos, wid, hei, Notepad
Msgbox, Notepad at %xpos% %ypos% %wid% %hei% `nscreen = %A_ScreenWidth% x %A_ScreenHeight%
return

; main screen 1920w x 1080h
; half is 960w x 540h
; original winmove: WinMove, %WinTitle%,, (A_ScreenWidth/2)-(wid/2), (A_ScreenHeight/2)-(hei/2), 200,200
; save this one: WinMove, %WinTitle%,, (A_ScreenWidth/2), (A_ScreenHeight/2), 200,200