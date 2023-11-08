import { createRouter, createWebHistory } from "vue-router";
import HomeComponent from './components/HomeComponent';
import ComoDonar from './components/ComoDonar';
import ComntactoComponent from './components/ContactoComponent';
import QuienesSomos from './components/QuienesSomos';
import SponsorsComponent from './components/SponsorsComponent';
import FormularioComponent from './components/FormularioComponent';
import FundacionesComponent from './components/FundacionesComponent';
import ThankyouComponent from './components/ThankyouComponent';

// Acá definimos las rutas
const routes = [

    {
        path: '/',
        name: 'home',
        component: HomeComponent
    },
    {
        path: '/como-donar',
        name: 'Como Donar',
        component: ComoDonar
    },
    {
        path: '/contacto',
        name: 'Contacto',
        component: ComntactoComponent
    },
    {
        path: '/quienes-somos',
        name: 'Quienes Somos',
        component: QuienesSomos
    },
    {
        path: '/sponsors',
        name: 'Sponsors',
        component: SponsorsComponent
    },
    {
        path: '/formulario',
        name: 'Formulario',
        component: FormularioComponent
    },
    {
        path: '/fundaciones',
        name: 'Fundaciones',
        component: FundacionesComponent
    },
    {
        path: '/thank-you',
        name: 'Thankyou',
        component: ThankyouComponent
    },


];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;