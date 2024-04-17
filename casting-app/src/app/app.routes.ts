import { Routes } from '@angular/router';
import { NotFoundComponent } from './not-found/not-found.component';
import { HomeComponent } from './home/home.component';
import { FormComponent } from './form/form.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { AdsComponent } from './ads/ads.component';
import { CastingComponent } from './casting/casting.component';
import { Observable } from 'rxjs';
import {ModelingComponent} from "./modeling/modeling.component";
import {FilmingComponent} from "./filming/filming.component";
import {DanceComponent} from "./dance/dance.component";

export const routes: Routes = [

    {path : '', redirectTo: 'home', pathMatch: 'full'},
    {path : 'home',  component:  HomeComponent , title: 'Home page'},
    {path : 'aboutUs',  component:  AboutUsComponent, title: 'About us'},
    {path : 'form',  component: FormComponent , title: 'Form page'},
    {path : 'ads',  component:  AdsComponent , title: 'Ads'},
    {path : 'casting',  component:  CastingComponent, title: 'Casting'},
    {path : 'casting/modeling',  component:  ModelingComponent, title: 'Casting'},
    {path : 'casting/filming',  component:  FilmingComponent, title: 'Casting'},
    {path : 'casting/dance',  component:  DanceComponent, title: 'Casting'},
    {path : 'logIn',  component:  HomeComponent , title: 'Log in'},
    // {path : 'casting/:id', component:  CastingComponent, title: ''},
    {path : '**', component: NotFoundComponent , title: '404 Not Found'},

];

const locations = new Observable((observer) => {

});
