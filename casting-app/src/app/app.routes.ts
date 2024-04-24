import { Routes } from '@angular/router';
import { NotFoundComponent } from './components/not-found/not-found.component'; 
import { HomeComponent } from './components/home/home.component';
import { FormComponent } from './components/form/form.component';
import { AboutUsComponent } from './components/about-us/about-us.component';
import { AdsComponent } from './components/ads/ads.component';
import { CastingComponent } from './components/casting/casting.component';
import { Observable } from 'rxjs';
import {ModelingComponent} from "./components/modeling/modeling.component";
import {FilmingComponent} from "./components/filming/filming.component";
import {DanceComponent} from "./components/dance/dance.component";
import { CastingDetailsComponent } from './components/casting-details/casting-details.component';

export const routes: Routes = [

    {
        path : '', 
        redirectTo: 'home', 
        pathMatch: 'full'
    },
    {
        path : 'home',  
        component:  HomeComponent , 
        title: 'Home page'
    },
    {
        path : 'aboutUs',  
        component:  AboutUsComponent, 
        title: 'About us'
    },
    {
        path : 'form',  
        component: FormComponent , 
        title: 'Form page'
    },
    {
        path : 'ads',  
        component:  AdsComponent , 
        title: 'Ads'
    },
    {
        path : 'casting',  
        component:  CastingComponent, 
        title: 'Casting'
    },
    {
        path : 'casting/modeling',  
        component:  ModelingComponent, 
        title: 'Casting'
    },
    {
        path : 'casting/filming',  
        component:  FilmingComponent, 
        title: 'Casting'
    },
    {
        path : 'casting/dance',  
        component:  DanceComponent, 
        title: 'Casting'
    },
    // {
    //     path : 'logIn',  
    //     component:  HomeComponent , 
    //     title: 'Log in'
    // },
    {
        path : 'casting/:id', 
        component:  CastingDetailsComponent, 
    },
    {
        path : '**', 
        component: NotFoundComponent 
    },

];

const locations = new Observable((observer) => {

});
