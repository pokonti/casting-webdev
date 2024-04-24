import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Casting } from '../interfaces/api';

@Injectable({
  providedIn: 'root'
})
export class AllservicesService {

  private BASE_URL: string = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient ) {}

  getAllCastings(){
    return this.http.get<Casting[]>(`${this.BASE_URL}/castings`)
  }


}
