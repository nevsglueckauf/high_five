from smda.find_loc import LocationFinder


foo = LocationFinder()

dta = foo.snd_req(cty='Bochum', obj='supermarket')

print(vars(dta.lst_rsp))
