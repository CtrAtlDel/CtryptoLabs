ORG 8000H
IEN0 EQU 0A8H
LJMP START

ORG 8003H ;обработчик прерывания INT0
RETI
ORG 800BH    ;обработчик прерывания при переполнении таймера Т0
    CLR TF0  ;сброс флага переполнения таймера Т0
    INC DPTR ;увеличение программного счетчика
    MOV A,DPH
    SWAP A ;для корректного отображения на индикаторе
    MOV 0C0h,A  ;вывод старшего байта программного счетчика на индикацию
RETI ;возвращается на адрес, сохраненный в RETI
START:
    MOV IE,#82h ;разрешение прерывания при переполнении таймера Т0
    MOV DPTR,#0000h ;сброс программного счетчика
    LJMP $     ;безусловный переход, предварительно сохранив значение адреса команды в стек вызовов
    CLR TR0 ;сброс бита разрешения таймера Т0
    CLR TF0 ;сброс флага переполнения таймера Т0
    MOV TL0, #00h
    MOV TH0, #00h
    MOV TMOD,#09h ;Т0 таймер в режиме 1 с запуском по единичному значению на входе INT0
    SETB TR0   ;разрешение работы таймера Т0
END
;-----------------------------------------------------
MOV IEN0, #84H ;разрешение прерывания INT1
MOV DPTR,#7FFFh
  MOV A,#01h   ;Очистка экрана ЖКИ
MOVX @DPTR,A ;ввод символа слева,
 ;декодированный режим
LCALL DINIT
AJMP MENU
BEGIN: 
LJMP M2
ORG 8013h  ;обработчик прерывания INT1
    MOV DPTR,#7FFFh
    MOV A,#40h
    MOVX @DPTR,A ;разрешение чтения FIFO
    ;клавиатуры
    MOV DPTR,#7FFEh
    MOVX A,@DPTR ;чтение скан-кода
    CJNE A, #11011001B, K1 ;проверка скан-кода
    ;клавиши «0»
    MOV DPTR,#7FFEh
    MOV A,#11110011b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «0»
    MOV R4, #30H ; жки вывод
LCALL VIVOD
LJMP EXIT
K1: CJNE A, #11000000B, K2  ;проверка скан-кода
    ;клавиши «1»
    MOV DPTR,#7FFEh
    MOV A,#01100000b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «1» 
    MOV R4, #31H ; жки вывод
    LCALL VIVOD 
    LJMP EXIT
K2: CJNE A, #11000001B, K3  ;проверка скан-кода
    ;клавиши «2»
    MOV DPTR,#7FFEh
    MOV A,#10110101b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «2»
    MOV R4, #32H ; жки вывод
    LCALL VIVOD
    LJMP EXIT
K3: CJNE A, #11000010B, K4  ;проверка скан-кода
    ;клавиши «3»
    MOV DPTR,#7FFEh
    MOV A,#11110100b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «3»
    MOV R4, #33H ; жки вывод
    LCALL VIVOD
LJMP EXIT
K4: CJNE A, #11001000B, K5  ;проверка скан-кода
    ;клавиши «4»
    MOV DPTR,#7FFEh
    MOV A,#01100110b
    MOVX @DPTR,A  ;вывод в видеопамять кода
    ;символа «4»
    MOV R4, #34H ; жки вывод
    LCALL VIVOD
LJMP EXIT
K5: CJNE A, #11001001B, K6   ;проверка скан-кода
    ;клавиши «5»
    MOV DPTR,#7FFEh
    MOV A,#11010110b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «5»
    MOV R4, #35H ; жки вывод
    LCALL VIVOD 
LJMP EXIT
K6: CJNE A, #11001010B, K7  ;проверка скан-кода
    ;клавиши «6»
    MOV DPTR,#7FFEh
    MOV A,#11010111b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «6»
    MOV R4, #36H ; жки вывод
    LCALL VIVOD 
LJMP EXIT
K7: CJNE A, #11010000B, K8  ;проверка скан-кода
    ;клавиши «7»
    MOV DPTR,#7FFEh
    MOV A,#01110000b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «7»
    MOV R4, #37H ; жки вывод
    LCALL VIVOD 
LJMP EXIT
K8: CJNE A, #11010001B, K9 ;проверка скан-кода
    ;клавиши «8»
    MOV DPTR,#7FFEh
    MOV A,#11110111b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «8»
    MOV R4, #38H ; жки вывод
    LCALL VIVOD 
LJMP EXIT
K9: CJNE A, #11010010B, K10 ;проверка скан-кода
    ;клавиши «9»
    MOV DPTR,#7FFEh
    MOV A,#11110110b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «9»
    MOV R4, #39H ; жки вывод
    LCALL VIVOD 
LJMP EXIT
K10: 
CJNE A, #11000011B, K11 ;проверка скан-кода
    ;клавиши «A»
    MOV DPTR,#7FFEh 
    MOV A,#01110111b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «A»
    MOV R4, #41H ; жки вывод
    LCALL VIVOD 
LJMP EXIT
K11: CJNE A, #11001011B, K12 ;проверка скан-кода
    ;клавиши «B»
    MOV DPTR,#7FFEh
    MOV A,#11000111b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «B»
    MOV R4, #42H ; жки вывод
    LCALL VIVOD 
LJMP EXIT
K12: CJNE A, #11010011B, K13 ;проверка скан-кода
    ;клавиши «C»
    MOV DPTR,#7FFEh
    MOV A,#10010011b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «C»
    MOV R4, #43H ; жки вывод
    LCALL VIVOD 
LJMP EXIT
K13: CJNE A, #11011011B, K14 ;проверка скан-кода
    ;клавиши «D»
    MOV DPTR,#7FFEh
    MOV A,#11100101b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «D»
    MOV A,#02H ;переещение каретки в начало строки
    LCALL DINIT
    MOV A,#01H  ;очистка дисплея
    LCALL DINIT
LJMP EXIT
K14: CJNE A, #11011000B, K15 ;проверка скан-кода
    ;клавиши «*»
    MOV DPTR,#7FFEh
    MOV A,#10010111b
    MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «E»
    MOV R4, #45H ; жки вывод
    LCALL VIVOD 
LJMP EXIT
K15: CJNE A, #11011010B, EXIT ;проверка скан-кода
    ;клавиши «#»
    MOV DPTR,#7FFEh
    MOV A,#00010111b
    ;MOVX @DPTR,A ;вывод в видеопамять кода
    ;символа «F»
    ;MOV R4, #46H ; жки вывод
    MOV A,#02H ;переещение каретки в начало строки
    LCALL DINIT
    MOV A,#01H  ;очистка дисплея
LCALL DINIT
LCALL VIVOD
AJMP MENU2
Q: 
LJMP EXIT

EXIT:
RETI ;выход из обработчика
 ;прерывания INT1
M2:
MOV DPTR, #7FFFh
MOV A, #90h
MOVX @DPTR,A
LJMP $
;----------------------------------------------------
MENU: ;меню для отображения команд
MOVX @DPTR,A ;вывод в видеопамять кода символа «D»
MOV R4, #44H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «.»
MOV R4, #2EH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «C»
MOV R4, #43H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «L»
MOV R4, #4CH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «E»
MOV R4, #45H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «A»
MOV R4, #41H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «R»
MOV R4, #52H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа « »
MOV R4, #20H   ;жки вывод
LCALL VIVOD

MOVX @DPTR,A ;вывод в видеопамять кода символа «C»
MOV R4, #43H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «.»
MOV R4, #2EH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «S»
MOV R4, #53H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «T»
MOV R4, #54H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «A»
MOV R4, #41H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «R»
MOV R4, #52H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «T»
MOV R4, #54H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа « »
MOV R4, #20H   ;жки вывод
LCALL VIVOD

LCALL SPLIT ;перенос строки

MOVX @DPTR,A ;вывод в видеопамять кода символа «A»
MOV R4, #41H  ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «.»
MOV R4, #2EH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «A»
MOV R4, #41H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «D»
MOV R4, #44H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «D»
MOV R4, #44H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа « »
MOV R4, #20H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа « »
MOV R4, #20H   ;жки вывод
LCALL VIVOD


MOVX @DPTR,A ;вывод в видеопамять кода символа «B»
MOV R4, #42H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «.»
MOV R4, #2EH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «E»
MOV R4, #45H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «X»
MOV R4, #58H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «I»
MOV R4, #49H   ;жки вывод
LCALL VIVOD
  MOVX @DPTR,A ;вывод в видеопамять кода символа «T»
MOV R4, #54H   ;жки вывод
LCALL VIVOD
AJMP BEGIN
CLEAR:
MOV A,#01H   ;очистка дисплея
LCALL DINIT
MENU2: ;меню для отображения команд
MOVX @DPTR,A ;вывод в видеопамять кода символа «D»
MOV R4, #44H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «.»
MOV R4, #2EH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «C»
MOV R4, #43H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «L»
MOV R4, #4CH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «E»
MOV R4, #45H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «A»
MOV R4, #41H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «R»
MOV R4, #52H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа « »
MOV R4, #20H   ;жки вывод
LCALL VIVOD

MOVX @DPTR,A ;вывод в видеопамять кода символа «C»
MOV R4, #43H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «.»
MOV R4, #2EH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «S»
MOV R4, #53H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «T»
MOV R4, #54H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «A»
MOV R4, #41H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «R»
MOV R4, #52H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «T»
MOV R4, #54H   ;жки вывод
LCALL VIVOD

LCALL SPLIT ;перенос строки

MOVX @DPTR,A ;вывод в видеопамять кода символа «A»
MOV R4, #41H  ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «.»
MOV R4, #2EH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «A»
MOV R4, #41H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «D»
MOV R4, #44H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «D»
MOV R4, #44H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа « »
MOV R4, #20H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа « »
MOV R4, #20H   ;жки вывод
LCALL VIVOD


MOVX @DPTR,A ;вывод в видеопамять кода символа «B»
MOV R4, #42H  ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «.»
MOV R4, #2EH   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «E»
MOV R4, #45H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «X»
MOV R4, #58H   ;жки вывод
LCALL VIVOD
MOVX @DPTR,A ;вывод в видеопамять кода символа «I»
MOV R4, #49H   ;жки вывод
LCALL VIVOD
  MOVX @DPTR,A ;вывод в видеопамять кода символа «T»
MOV R4, #54H   ;жки вывод
LCALL VIVOD
  LJMP EXIT
AJMP Q
;----------------------------------------------------
;ADDWORD:
;SUMCHAR:
;----------------------------------------------------
SPLIT:
    MOV A, #38H ;см функцию VIVOD
    LCALL DINIT
    MOV A, #0CH
    LCALL DINIT
    MOV A, #06H
    LCALL DINIT
    MOV DPTR, #7FF6H
WAITING:
    MOVX A, @DPTR
    ANL A, #80H
    JNZ WAITING
    MOVX A, @DPTR
    CJNE A, #10H, MAX
SECOND:
    MOV A,#0A8H
    LCALL DINIT
    MOV DPTR, #7FF6H
    JMP OUT
MAX:
    JC SECOND
    MOV A, #80H
    LCALL DINIT
    MOV DPTR, #7FF6H
OUT:
    MOVX A, @DPTR
    ANL A, #80H
    JNZ OUT
;----------------------------------------------------
VIVOD:
    MOV A,#38H  ;две строки размер символа 5*8 точек
    LCALL DINIT ;вызов подпрограммы записи команды в
    ;управляющий регистр дисплея
    MOV A,#0CH  ;включение дисплея
    LCALL DINIT
    MOV A,#06H  ;сдвиг курсора вправо после вывода
    ;символа
    LCALL DINIT
    ;MOV A,#02H  ;переещение каретки в начало строки
    ;LCALL DINIT
    ;MOV A,#01H  ;очистка дисплея
    ;LCALL DINIT
    MOV A,R4 ;код символа из R4 в аккумулятор
    LCALL DISP  ;вызов подпрограммы записи кода
    ;символа в регистр данных дисплея
RET
DINIT:
    MOV R0,A
    MOV DPTR,#7FF6H ;ожидание установки флага завершения записи в память дисплея
BF:
    MOVX A,@DPTR
    ANL A,#80H
    JNZ BF
    MOV DPTR,#7FF4H ;запись кода команды в управляющий регистр дисплея 
    MOV A,R0
    MOVX @DPTR,A
RET
DISP:
    MOV R0,A
    MOV DPTR,#7FF6H ;ожидание установки флага завершения записи в память дисплея
BF1:
    MOVX A,@DPTR
    ANL A,#80H
    JNZ BF1
    MOV DPTR,#7FF5H ;запись значения кода символа в регистр данных дисплея
    MOV A,R0
    MOVX @DPTR,A
RET

END