import { Component, OnInit } from '@angular/core';
import { AllservicesService } from '../../services/allservices.service';
import { Casting } from '../../interfaces/api';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dance',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './dance.component.html',
  styleUrl: './dance.component.css'
})
export class DanceComponent implements OnInit{

  castings: Casting[] = [];
  filterName: string = 'Dance';

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
