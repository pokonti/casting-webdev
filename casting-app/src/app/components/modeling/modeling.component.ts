import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { Casting } from '../../interfaces/api';
import { AllservicesService } from '../../services/allservices.service';

@Component({
  selector: 'app-modeling',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './modeling.component.html',
  styleUrl: './modeling.component.css'
})
export class ModelingComponent implements OnInit{
  castings: Casting[] = [];
  filterName: string = 'Modeling';

  constructor(private myService: AllservicesService) {}
  
  ngOnInit(): void {
    this.filterCastingsByName()
  }

  filterCastingsByName(): void {
    this.myService.getFilteredCastingsByName(this.filterName)
      .subscribe(
        (castings: Casting[]) => {
          this.castings = castings;
          // console.log('Filtered Castings:', this.castings);
        },
        (error) => {
          console.error('Error fetching castings:', error);
        }
      );
  }
}
