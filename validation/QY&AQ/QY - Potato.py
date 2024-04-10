import os

import cobra
import pandas as pd
from cobra.flux_analysis import pfba

from tests import TEST_DIR


def QY_AQ(non_diel_model, diel_model):
    fba_sol_nd = pfba(non_diel_model).fluxes
    fba_sol_d = pfba(diel_model).fluxes

    return fba_sol_nd, fba_sol_d


if __name__ == '__main__':
    original_model = cobra.io.read_sbml_model(os.path.join(TEST_DIR, 'models', 'potato_mat.xml'))
    diel_potato_model = cobra.io.read_sbml_model(os.path.join(TEST_DIR, 'models', "diel_potato_model.xml"))

    original_model.objective = "RBS01"
    original_model.objective_direction = "max"
    diel_potato_model.objective = "Biomass_Total"
    diel_potato_model.objective_direction = "max"

    fba_sol_non_diel, fba_sol_diel_model = QY_AQ(original_model, diel_potato_model)


    data_quantum_assimilation = {
        'Quantum Yield': [fba_sol_non_diel["R00024"] / - fba_sol_non_diel["RB002"],
                          fba_sol_diel_model["R00024_Day"] / - fba_sol_diel_model["RB002_Day"]]}

    #,'Assimilation Quotient': [fba_sol_non_diel["R00024_p"] / fba_sol_non_diel["XXX"],fba_sol_diel_model["R00024_p_Day"] / fba_sol_diel_model["XXX"]]}

    tabel = pd.DataFrame(data_quantum_assimilation)

    tabel.index = ["Original Model", "Created Diel Model"]

    tabel.to_csv('QY_potato.csv', sep=',')

    print(tabel)