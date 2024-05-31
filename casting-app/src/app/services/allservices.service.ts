import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Ad, Casting, Position } from '../interfaces/api';
import { map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AllservicesService {

  private BASE_URL: string = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient ) {}

  getAllCastings(){
    return this.http.get<Casting[]>(`${this.BASE_URL}/castings`)
  }

  getFilteredCastingsByName(name: string) {
    return this.http.get<Casting[]>(`${this.BASE_URL}/castings`).pipe(
      map((castings: Casting[]) => {
        return castings.filter(casting => casting.name.toLowerCase() === name.toLowerCase());
      })
    );
  }

  getCastingDetail(id: number){
    return this.http.get<Casting>(`${this.BASE_URL}/castings/${id}`)
  }
  getPositionsByCasting(id: number){
    return this.http.get<Position[]>(`${this.BASE_URL}/castings/${id}/positions`)
  }

  getPositionById(id: number){
    return this.http.get<Position>(`${this.BASE_URL}/positions/${id}`)
  }

  getAds(){
    return this.http.get<Ad[]>(`${this.BASE_URL}/ads`)
  }

}
