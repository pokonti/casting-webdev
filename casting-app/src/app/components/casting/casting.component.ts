import { Component, OnInit } from '@angular/core';
import { Casting } from '../../interfaces/api';
import { AllservicesService } from '../../services/allservices.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-casting',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './casting.component.html',
  styleUrl: './casting.component.css'
})
export class CastingComponent implements OnInit{
  castings: Casting[] = [];

  constructor(private myService: AllservicesService){}
  
  ngOnInit(): void {
    this.getCastingsList()
  }

  getCastingsList(){
    this.myService.getAllCastings().subscribe((castings) => {
      this.castings = castings;
    });
  }


}
