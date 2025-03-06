import os

import cobra
import pandas as pd
from cobra.flux_analysis import pfba

def QY(non_diel_model, diel_model):
    fba_sol_nd = pfba(non_diel_model).fluxes
    fba_sol_d = pfba(diel_model).fluxes

    return fba_sol_nd, fba_sol_d


if __name__ == '__main__':
    original_model = cobra.io.read_sbml_model(os.path.join("..", "..", "..", "examples", 'models', 'Maize_Saha2011_v2.xml'))
    diel_maize_saha_model = cobra.io.read_sbml_model(os.path.join("..", "..", "..", "examples", 'models', "diel_maize_saha_model_wo_nitrate.xml"))

    lb = pfba(original_model).fluxes["Biomass_synthesis"]
    original_model.objective = "EX_hv"
    original_model.objective_direction = "max"
    original_model.reactions.Biomass_synthesis.bounds = (lb, 1000)

    lb_diel = pfba(diel_maize_saha_model).fluxes["Biomass_Total"]
    diel_maize_saha_model.objective = "EX_hv_Day"
    diel_maize_saha_model.objective_direction = "max"
    diel_maize_saha_model.reactions.Biomass_Total.bounds = (lb_diel, 1000)

    fba_sol_non_diel, fba_sol_diel_model = QY(original_model, diel_maize_saha_model)

    data_quantum_assimilation = {
        'Quantum Yield': [fba_sol_non_diel["R00024_p"] / - fba_sol_non_diel["EX_hv"],
                          fba_sol_diel_model["R00024_p_Day"] / - fba_sol_diel_model["EX_hv_Day"]]}

    tabel = pd.DataFrame(data_quantum_assimilation)

    tabel.index = ["Original Model", "Created Diel Model"]

    tabel.to_csv('QY_maize_saha.csv', sep=',')

    print(tabel)