
####
# we define all the restrition functions here!!!
#in all functions, we are working with m = matrix = the table of schedule
###

#restrition 1: It is necessary to have a minimum of 1 nurse and a maximum of 3 nurses on each shift.
#for this restrition, we made:
#   - -1 fit for each nurse overschedule
#   - -1 fit for non nurse in a shift
def restrition1(m):
    fit = 0

    for n_shift in range(len(m[0])):
        cont = 0

        for nurse in m:
            if nurse[n_shift] == 1:
                cont+=1
        if cont < 1:
            fit += 1
        elif cont > 3:
            fit = cont - 3
    return fit*-1


#Restrition2: Each nurse should be assigned to 5 shifts per week
# for each nurse with shift != 5, fit decrement -1
def restrition2(m):
    fit = 0
    for nurse in m:
        cont = 0
        for shift in nurse:
            if shift == 1:
                cont+=1
        if cont != 5:
            fit -=1
    return fit

#Restrition3: No nurse can work more than 3 consecutive days without a day off
# For this role, we schedule a fit for each nurse who works 3 consecutive days.
#  The rest interval for a nurse is 3 consecutive free shifts.
def restrition3(m):
    fit = 0
    for nurse in m:

        #two counters to verify the interval
        cont_0 = 0
        cont = 0
        for shift in nurse:
            if cont > 9:
                fit -=1
                break

            if shift == 1 and cont == 0:
                cont +=1
                cont_0 = 0
                continue

            if shift == 1 and cont != 0:
                cont +=1
                cont_0 = 0
                continue

            if shift == 0 and cont != 0:
                cont += 1
                cont_0 += 1
                if cont_0 == 3:
                    cont = 0
                    cont_0 = 0
                continue
        if cont > 9:
            fit -=1
    return fit


#restrition4: Nurses prefer consistency in their schedules,
#  meaning they prefer working the same shift (day, night, or overnight) 
# every day of the week.
                

m = [[1,1,1,1,1,1,1,1,1,1], [1,1,0,1,1,0,0,0,0,1], [1,1,0,1,0,1,1,1,1,1], [1,1,0,1,1,1,0,0,1,0]]

print(restrition3(m))